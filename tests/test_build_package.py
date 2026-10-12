import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.verify_history import ROOT


class BuildValidation(unittest.TestCase):
    def test_untracked_local_metadata_is_not_packaged(self):
        with TemporaryDirectory(dir=ROOT / "profile") as directory:
            Path(directory, ".DS_Store").write_bytes(b"local metadata")
            result = subprocess.run(
                [sys.executable, "-m", "scripts.build_package"],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_optimized_python_cannot_skip_package_validation(self):
        result = subprocess.run(
            [sys.executable, "-O", "-m", "scripts.build_package"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Package verification requires Python without -O", result.stderr)


if __name__ == "__main__":
    unittest.main()
