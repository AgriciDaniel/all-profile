import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills/all-profile/scripts/count_text.py"
spec = importlib.util.spec_from_file_location("counter", SCRIPT)
counter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(counter)


class CountTextTests(unittest.TestCase):
    def test_emoji_is_not_one_utf16_unit(self):
        self.assertEqual(counter.count_text("🛠️"), {
            "unicode_code_points": 2, "utf16_code_units": 3,
            "utf8_bytes": 7, "lf_characters": 0, "cr_characters": 0,
        })

    def test_exact_newlines_and_combining_marks(self):
        result = counter.count_text("e\u0301\r\n")
        self.assertEqual(result["unicode_code_points"], 4)
        self.assertEqual(result["lf_characters"], 1)
        self.assertEqual(result["cr_characters"], 1)

    def test_empty(self):
        self.assertTrue(all(v == 0 for v in counter.count_text("").values()))

    def test_cli_preserves_trailing_newline(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "-"], input=b"a\n",
                                capture_output=True, check=True)
        import json
        self.assertEqual(json.loads(result.stdout)["unicode_code_points"], 2)

    def test_reject_invalid_utf8(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "-"], input=b"\xff",
                                capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, b"")


if __name__ == "__main__":
    unittest.main()
