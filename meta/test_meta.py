# -*- coding: utf-8 -*-
"""生成器与校验器的本地回归测试；只使用 Python 标准库。"""

import contextlib
import io
import os
import pathlib
import tempfile
import unittest
from unittest import mock

import build
import check


class ReadmeRenderingTests(unittest.TestCase):
    def test_readme_uses_compact_catalog_when_rendered(self):
        _, outputs = build.render_outputs()

        readme = outputs["README.md"]

        self.assertIn("# AI 重构软件 · 一手材料清单", readme)
        self.assertIn("不收录仅讨论模型能力", readme)
        self.assertIn("正式收录须同时通过三道门", readme)
        self.assertIn("权威性用于判断证据强度和主张边界", readme)
        self.assertIn("[分类口径](#怎么分类)", readme)
        self.assertIn("rg 'MCP' index.tsv", readme)
        self.assertIn("[`meta/policy.py`](meta/policy.py)", readme)
        self.assertIn("| 日期 | 材料 | 出品方 | 分类 |", readme)
        self.assertIn("摘要：提出用计算机操作智能体模拟用户需求", readme)
        self.assertIn("收录理由：", readme)
        self.assertIn("收录理由说明材料为何在本目录", readme)
        self.assertIn("**主题** `安全与攻防` `界面与接入`<br>**标签**", readme)
        self.assertIn("| 英文标签 | 中文别名 | 条目数 |", readme)
        self.assertNotIn("<br>Salesforce · 文章 · 厂商", readme)

    def test_index_preserves_separate_topic_and_tag_columns_when_rendered(self):
        _, outputs = build.render_outputs()

        header = outputs["index.tsv"].splitlines()[0]

        self.assertEqual(
            header,
            "首发日期\t最后更新\t标题\t出品方\t体裁\t出品方类型\t主题\t标签\t出处\t摘要\t收录理由",
        )


class GeneratedOutputTests(unittest.TestCase):
    def test_write_outputs_replaces_all_targets_when_content_is_valid(self):
        outputs = {
            "README.md": "readme\n",
            "index.tsv": "a\tb\n1\t2\n",
            "fetch.sh": "#!/usr/bin/env bash\n",
        }
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(build, "ROOT", directory):
            build.write_outputs(outputs)

            actual = {
                name: pathlib.Path(directory, name).read_text(encoding="utf-8")
                for name in outputs
            }
            executable = os.access(pathlib.Path(directory, "fetch.sh"), os.X_OK)

        self.assertEqual(actual, outputs)
        self.assertTrue(executable)

    def test_main_preserves_outputs_when_prewrite_validation_fails(self):
        sentinels = {
            "README.md": "old readme\n",
            "index.tsv": "old index\n",
            "fetch.sh": "old fetch\n",
        }
        with tempfile.TemporaryDirectory() as directory:
            for name, content in sentinels.items():
                pathlib.Path(directory, name).write_text(content, encoding="utf-8")
            generated = {name: "new\n" for name in sentinels}
            generated["index.tsv"] = ""
            with (mock.patch.object(build, "ROOT", directory),
                  mock.patch.object(build.check, "run", return_value=[]),
                  mock.patch.object(build, "render_outputs", return_value=([object()], generated)),
                  contextlib.redirect_stdout(io.StringIO())):
                with self.assertRaises(SystemExit):
                    build.main()

            actual = {
                name: pathlib.Path(directory, name).read_text(encoding="utf-8")
                for name in sentinels
            }

        self.assertEqual(actual, sentinels)

    def test_check_written_outputs_reports_drift_when_readme_changed(self):
        outputs = {
            "README.md": "expected\n",
            "index.tsv": "a\tb\n1\t2\n",
            "fetch.sh": "#!/usr/bin/env bash\n",
        }
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(build, "ROOT", directory):
            build.write_outputs(outputs)
            pathlib.Path(directory, "README.md").write_text("stale\n", encoding="utf-8")

            problems = build.check_written_outputs(outputs)

        self.assertEqual(problems, ["README.md 与生成源不一致；请运行 python3 meta/build.py"])


class ValidationTests(unittest.TestCase):
    def test_check_data_rejects_missing_collection_rationale(self):
        rows = check._rows()
        rows[0]["rationale"] = ""

        with mock.patch.object(check, "_rows", return_value=rows):
            problems = check.check_data()

        self.assertTrue(any("收录理由必须是单段" in problem for problem in problems))

    def test_check_generated_freshness_reports_action_when_subprocess_times_out(self):
        with mock.patch.object(
                check.subprocess, "run", side_effect=check.subprocess.TimeoutExpired("build", 30)):
            problems = check.check_generated_freshness()

        self.assertEqual(len(problems), 1)
        self.assertIn("超过 30 秒", problems[0])
        self.assertIn("单独运行", problems[0])

    def test_check_fetched_reports_action_when_url_differs(self):
        row = {
            "first": "2026-01-01",
            "updated": "-",
            "title": "Example",
            "org": "Example",
            "genre": "文档",
            "org_kind": "厂商",
            "topics": ["构造方式"],
            "tags": ["MCP"],
            "url": "https://example.com/current",
            "key": "example",
        }
        fetched = (
            "名称\t原始类型\t抓取日期\t出处地址\n"
            "example\thtml\t2026-01-01\thttps://example.com/old\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            pathlib.Path(directory, "fetched.tsv").write_text(fetched, encoding="utf-8")
            with (mock.patch.object(check, "HERE", directory),
                  mock.patch.object(check, "_rows", return_value=[row])):
                problems = check.check_fetched()

        self.assertEqual(len(problems), 1)
        self.assertIn("请重新核对后同步两处地址", problems[0])

    def test_check_fetched_reports_action_when_header_is_malformed(self):
        fetched = "名称\t抓取日期\nexample\t2026-01-01\n"
        with tempfile.TemporaryDirectory() as directory:
            pathlib.Path(directory, "fetched.tsv").write_text(fetched, encoding="utf-8")
            with mock.patch.object(check, "HERE", directory):
                problems = check.check_fetched()

        self.assertEqual(len(problems), 1)
        self.assertIn("请恢复四列表头", problems[0])


if __name__ == "__main__":
    unittest.main()
