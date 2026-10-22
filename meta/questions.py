"""问题数据与校验；与材料收录候选完全独立。"""
import json
import re
from pathlib import Path
from datetime import date
from catalog import TOPICS
from urllib.parse import urlsplit
STATUSES = ("待澄清", "待研究", "已转研究", "搁置")
KINDS = ("解释型", "决策型")
PLACEHOLDERS = {"其他", "其它", "不知道", "未知", "待定", "暂无", "待补充", "其他方案", "其他解释", "其他不知道"}


def normalized_content(text):
    return re.sub(r"[\W_]+", "", text).casefold()


def check_options(question, key):
    errors = []
    if question.get("kind") not in KINDS:
        errors.append(f"{key} 问题类型须为解释型或决策型")
    options = question.get("options")
    if not isinstance(options, list):
        return errors + [f"{key} options 必须为数组；待澄清可为空"]
    ids, contents = set(), set()
    for option in options:
        if not isinstance(option, dict):
            errors.append(f"{key} 候选选项必须为对象")
            continue
        option_id = option.get("id")
        if not isinstance(option_id, str) or not re.fullmatch(r"[A-Z][A-Z0-9-]*", option_id) or option_id in ids:
            errors.append(f"{key} 选项编号无效或重复")
        if isinstance(option_id, str):
            ids.add(option_id)
        for field in ("content", "basis", "evidence_needed"):
            if not isinstance(option.get(field), str) or not option[field].strip():
                errors.append(f"{key}/{option_id} 缺少 {field}")
        content = normalized_content(option.get("content", "")) if isinstance(option.get("content"), str) else ""
        if len(content) < 8 or content in PLACEHOLDERS:
            errors.append(f"{key}/{option_id} 需实质候选解释或方案，不能用其他或不知道凑数")
        elif content in contents:
            errors.append(f"{key}/{option_id} 候选内容重复")
        else:
            contents.add(content)
        for field in ("conditions", "cost"):
            if field not in option or (option[field] is not None and (not isinstance(option[field], str) or not option[field].strip())):
                errors.append(f"{key}/{option_id} {field} 须为说明文字；未知用 null")
    if question.get("status") == "待研究" and len(contents) < 2:
        errors.append(f"{key} 待研究至少须有两个实质不同的候选解释或方案；否则留在待澄清")
    return errors

def valid_url(value):
    try:
        parsed = urlsplit(value)
        parsed.port  # Access validates a numeric port and its legal range.
        return isinstance(value, str) and not re.search(r"\s", value) and parsed.scheme == "https" and bool(parsed.hostname) and not parsed.username and not parsed.password
    except (ValueError, TypeError, AttributeError):
        return False


def check_references(question, key):
    errors = []
    sources = question.get("sources", [])
    ids = set()
    for source in sources if isinstance(sources, list) else []:
        if not isinstance(source, dict):
            continue
        source_id = source.get("id")
        if not isinstance(source_id, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", source_id) or source_id in ids:
            errors.append(f"{key} 来源 ID 无效或重复")
        if isinstance(source_id, str):
            ids.add(source_id)
        if not valid_url(source.get("url")):
            errors.append(f"{key} 来源 URL 无效")
    def references(owner, field, required=False):
        values = owner.get(field)
        if not isinstance(values, list) or (required and not values):
            errors.append(f"{key} {field} 须为引用数组" + ("且不得为空" if required else ""))
            return
        seen = set()
        for value in values:
            if not isinstance(value, str) or value not in ids or value in seen:
                errors.append(f"{key} {field} 有不存在或重复的引用")
            if isinstance(value, str):
                seen.add(value)
    for field in ("basis_refs", "known_refs", "next_step_refs"):
        references(question, field)
    options = question.get("options", [])
    for option in options if isinstance(options, list) else []:
        if isinstance(option, dict):
            for field in ("basis_refs", "evidence_refs", "counter_refs", "target_refs"):
                references(option, field)
    checks = question.get("checks")
    if not isinstance(checks, list):
        errors.append(f"{key} checks 须为数组；尚未查证时为空")
    else:
        check_ids = set()
        for record in checks:
            if not isinstance(record, dict):
                errors.append(f"{key} 查证记录无效"); continue
            check_id = record.get("id")
            if not isinstance(check_id, str) or not re.fullmatch(r"V-\d{3,}", check_id) or check_id in check_ids:
                errors.append(f"{key} 查证编号无效或重复")
            if isinstance(check_id, str):
                check_ids.add(check_id)
            try:
                if not isinstance(record.get("date"), str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", record["date"]):
                    raise ValueError("invalid date shape")
                date.fromisoformat(record["date"])
            except (ValueError, TypeError):
                errors.append(f"{key} 查证日期无效")
            if not isinstance(record.get("result"), str) or not record["result"].strip():
                errors.append(f"{key} 查证结果无效")
            references(record, "source_refs", required=True)
    return errors


def load_questions():
    return json.loads(Path(__file__).with_name("questions.json").read_text(encoding="utf-8"))
def validate(data):
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("questions"), list):
        return ["问题数据版本或 questions 数组无效"]
    vocabulary = data.get("tag_vocabulary")
    if not isinstance(vocabulary, dict):
        errors.append("问题标签须提供受控 tag_vocabulary")
        vocabulary = {}
    labels = set()
    for tag_id, label in vocabulary.items():
        if not isinstance(tag_id, str) or not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", tag_id) or not isinstance(label, str) or not label.strip() or label != label.strip() or label in labels or label in (*TOPICS, *STATUSES, *KINDS):
            errors.append("问题标签词表有空白、重复或与主题/状态/类型混用")
        if isinstance(label, str):
            labels.add(label)
    ids = set()
    def valid_date(value):
        try:
            return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)) and bool(date.fromisoformat(value))
        except (ValueError, TypeError):
            return False
    for q in data["questions"]:
        if not isinstance(q, dict):
            errors.append("问题必须为对象"); continue
        key = q.get("id", "")
        if not isinstance(key, str) or not re.fullmatch(r"Q-\d{4,}", key) or key in ids:
            errors.append("问题编号无效或重复：" + str(key))
        if isinstance(key, str):
            ids.add(key)
        for field in ("title", "basis", "value", "known", "unknown", "next_step"):
            if not isinstance(q.get(field), str) or not q[field].strip():
                errors.append(f"{key} 缺少 {field}")
        if q.get("status") not in STATUSES or not valid_date(q.get("updated")):
            errors.append(f"{key} 状态或日期无效")
        errors += check_options(q, key)
        errors += check_references(q, key)
        for field, allowed in (("topics", TOPICS), ("tags", vocabulary)):
            values = q.get(field)
            if not isinstance(values, list) or not values or (field == "tags" and len(values) > 5):
                errors.append(f"{key} {field} 须为非空数组；每项最多五个议题标签")
                continue
            seen_values = set()
            for value in values:
                if not isinstance(value, str) or not value.strip() or value != value.strip() or value in seen_values or value not in allowed:
                    errors.append(f"{key} {field} 存在非法、空白或重复值")
                if isinstance(value, str):
                    seen_values.add(value)
        sources = q.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{key} 缺少来源")
        else:
            for source in sources:
                if not isinstance(source, dict) or not all(isinstance(source.get(f), str) and source[f].strip() for f in ("title", "url", "evidence")) or not source.get("url", "").startswith("https://") or not valid_date(source.get("checked")):
                    errors.append(f"{key} 来源无效")
        history = q.get("history")
        if not isinstance(history, list) or not history:
            errors.append(f"{key} 缺少历史")
        else:
            dates = []
            for revision in history:
                if not isinstance(revision, dict) or not valid_date(revision.get("date")) or not isinstance(revision.get("reason"), str) or not revision["reason"].strip():
                    errors.append(f"{key} 历史无效")
                else:
                    dates.append(revision["date"])
            if dates != sorted(dates) or (dates and dates[-1] != q.get("updated")):
                errors.append(f"{key} 历史与更新日期不一致")
        target = q.get("merged_into")
        if "merged_into" not in q or (target is not None and (not isinstance(target, str) or not re.fullmatch(r"Q-\d{4,}", target))):
            errors.append(f"{key} 合并去向格式无效")
        elif target and q.get("status") != "搁置":
            errors.append(f"{key} 合并旧项须搁置并保留历史")
    mapping = {q["id"]: q.get("merged_into") for q in data["questions"] if isinstance(q, dict) and isinstance(q.get("id"), str)}
    for key, target in mapping.items():
        seen = {key}
        while target:
            if not isinstance(target, str):
                errors.append(f"{key} 合并去向格式无效"); break
            if target not in mapping or target in seen:
                errors.append(f"{key} 合并去向不存在或循环"); break
            seen.add(target); target = mapping[target]
    return errors
