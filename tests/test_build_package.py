import subprocess
import sys
import unittest

from scripts.verify_history import ROOT


class BuildValidation(unittest.TestCase):
    def test_optimized_python_cannot_skip_package_validation(self):
        result = subprocess.run(
            [sys.executable, "-O", "-m", "scripts.build_package"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Package verification requires Python without -O", result.stderr)


if __name__ == "__main__":
    unittest.main()
