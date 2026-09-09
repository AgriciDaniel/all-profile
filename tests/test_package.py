"""Offline relocation checks; these do not test a host's skill discovery."""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "skills/all-profile"


class PackageTests(unittest.TestCase):
    def test_relocated_skill_is_self_contained(self):
        with tempfile.TemporaryDirectory(prefix="all-profile-test-") as directory:
            target = Path(directory) / "project/.agents/skills/all-profile"
            shutil.copytree(SOURCE, target)
            for markdown in target.rglob("*.md"):
                for match in re.finditer(r"\]\(([^)]+)\)", markdown.read_text()):
                    link = match.group(1)
                    if "://" in link or link.startswith("#"):
                        continue
                    resolved = (markdown.parent / link.split("#", 1)[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(target.resolve()), link)
                    self.assertTrue(resolved.is_file(), link)
            result = subprocess.run(
                [sys.executable, str(target / "scripts/count_text.py"), "-"],
                cwd=directory, input="🛠️\r\n".encode(), capture_output=True, check=True,
            )
            counts = json.loads(result.stdout)
            self.assertEqual(counts["unicode_code_points"], 4)
            self.assertEqual(counts["utf16_code_units"], 5)
            self.assertEqual(counts["cr_characters"], 1)
            self.assertEqual(counts["lf_characters"], 1)


if __name__ == "__main__":
    unittest.main()
