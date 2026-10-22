"""问题数据与校验；与材料收录候选完全独立。"""
import json
import re
from pathlib import Path
from datetime import date
STATUSES = ("待澄清", "待研究", "已转研究", "搁置")
def load_questions():
    return json.loads(Path(__file__).with_name("questions.json").read_text(encoding="utf-8"))
def validate(data):
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("questions"), list):
        return ["问题数据版本或 questions 数组无效"]
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
