import copy
import unittest
from questions import load_questions, validate

class QuestionValidationTests(unittest.TestCase):
    def test_seed_is_valid(self):
        self.assertEqual(validate(load_questions()), [])
    def test_rejects_invalid_status_date_and_source(self):
        data=copy.deepcopy(load_questions()); q=data["questions"][0]
        q.update(status="已解决", updated="2026-02-30", sources=[])
        self.assertGreaterEqual(len(validate(data)), 2)
    def test_rejects_duplicate_id(self):
        data=copy.deepcopy(load_questions()); data["questions"] *= 2
        self.assertTrue(any("重复" in e for e in validate(data)))
    def test_merge_requires_existing_target_without_cycle(self):
        for target in ("Q-9999", "Q-0001"):
            data=copy.deepcopy(load_questions()); data["questions"][0]["merged_into"]=target
            self.assertTrue(any("合并" in e for e in validate(data)))
    def test_history_must_match_updated(self):
        data=copy.deepcopy(load_questions()); data["questions"][0]["history"][-1]["date"]="2026-10-21"
        self.assertTrue(any("历史" in e for e in validate(data)))

    def test_merge_preserves_old_id_with_existing_destination(self):
        data=copy.deepcopy(load_questions()); other=copy.deepcopy(data["questions"][0]); other["id"]="Q-0002"
        data["questions"].append(other); data["questions"][0].update(status="搁置", merged_into="Q-0002")
        self.assertEqual(validate(data), [])
    def test_malformed_fields_return_errors(self):
        for field,value in (("id", 3),("merged_into", []),("history", [{}]),("sources", [None])):
            data=copy.deepcopy(load_questions()); data["questions"][0][field]=value
            self.assertTrue(validate(data))

    def test_research_needs_distinct_substantive_options(self):
        for options in ([], load_questions()["questions"][0]["options"][:1]):
            data=copy.deepcopy(load_questions()); data["questions"][0]["options"]=options
            self.assertTrue(any("至少" in e for e in validate(data)))
        data=copy.deepcopy(load_questions()); q=data["questions"][0]
        q["options"][1]["content"]=q["options"][0]["content"]
        self.assertTrue(any("重复" in e for e in validate(data)))
        q["options"][1]["content"]="其他／不知道"
        self.assertTrue(any("凑数" in e for e in validate(data)))
    def test_clarification_can_form_options_later(self):
        data=copy.deepcopy(load_questions()); q=data["questions"][0]
        q.update(status="待澄清", options=[], next_step="检索公开审查规则，访谈不同责任角色以形成并区分候选方案。")
        self.assertEqual(validate(data), [])
    def test_option_identity_and_evidence_are_required(self):
        for field,value in (("id", "A"),("evidence_needed", ""),("basis", ""),("conditions", 4)):
            data=copy.deepcopy(load_questions()); data["questions"][0]["options"][1][field]=value
            self.assertTrue(validate(data))
    def test_unknown_cost_and_conditions_can_be_explicit_null(self):
        data=copy.deepcopy(load_questions()); data["questions"][0]["options"][0].update(conditions=None,cost=None)
        self.assertEqual(validate(data), [])
    def test_question_kind_and_topic_and_tag_boundaries(self):
        for field,value in (("kind", "待研究"),("topics", ["待研究"]),("topics", ["安全与攻防", "安全与攻防"]),("tags", [" "]),("tags", ["human-review", "human-review"]),("tags", ["new-unknown-tag"])):
            data=copy.deepcopy(load_questions()); data["questions"][0][field]=value
            self.assertTrue(validate(data))
    def test_tag_registry_rejects_duplicate_labels_and_status_labels(self):
        for label in ("人工复核", "待研究", " 决策 ", ""):
            data=copy.deepcopy(load_questions()); data["tag_vocabulary"]["new-tag"]=label
            self.assertTrue(validate(data))
    def test_dangling_and_duplicate_references_fail(self):
        for refs in (["missing-source"], ["github-announcement", "github-announcement"]):
            data=copy.deepcopy(load_questions()); data["questions"][0]["basis_refs"]=refs
            self.assertTrue(any("引用" in e for e in validate(data)))
    def test_completed_verification_requires_sources(self):
        data=copy.deepcopy(load_questions()); data["questions"][0]["checks"][0]["source_refs"]=[]
        self.assertTrue(any("不得为空" in e for e in validate(data)))
    def test_missing_evidence_and_unstarted_checks_are_explicitly_allowed(self):
        data=copy.deepcopy(load_questions()); q=data["questions"][0]
        q["checks"]=[]; q["next_step_refs"]=[]
        q["options"][0].update(evidence_refs=[], counter_refs=[], target_refs=[])
        self.assertEqual(validate(data), [])
    def test_unsafe_or_malformed_source_urls_fail(self):
        for url in ("javascript:alert(1)", "https://", "https://user:password@example.com", "https://example.com/has space", "https://example.com:bad"):
            data=copy.deepcopy(load_questions()); data["questions"][0]["sources"][0]["url"]=url
            self.assertTrue(validate(data))
