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
        data=copy.deepcopy(load_questions()); data["questions"][0]["history"][0]["date"]="2026-10-21"
        self.assertTrue(any("历史" in e for e in validate(data)))

    def test_merge_preserves_old_id_with_existing_destination(self):
        data=copy.deepcopy(load_questions()); other=copy.deepcopy(data["questions"][0]); other["id"]="Q-0002"
        data["questions"].append(other); data["questions"][0].update(status="搁置", merged_into="Q-0002")
        self.assertEqual(validate(data), [])
    def test_malformed_fields_return_errors(self):
        for field,value in (("id", 3),("merged_into", []),("history", [{}]),("sources", [None])):
            data=copy.deepcopy(load_questions()); data["questions"][0][field]=value
            self.assertTrue(validate(data))
