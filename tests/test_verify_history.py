import io
import unittest
import warnings
import zipfile

from scripts.verify_history import read_package


def package(entries):
    result = io.BytesIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        with zipfile.ZipFile(result, "w") as archive:
            for name, data in entries:
                archive.writestr(name, data)
    result.seek(0)
    return result


class PackageValidation(unittest.TestCase):
    def test_accepts_original_text_entries(self):
        entries = [("export.r2x", b"{}"), ("BepInEx/config/example.cfg", b"[Test]\nEmpty = \n")]
        self.assertEqual(read_package(package(entries)), dict(entries))

    def test_rejects_unsafe_and_private_paths(self):
        for name in ("../outside.cfg", "/outside.cfg", "BepInEx\\config\\bad.cfg",
                     "BepInEx/config/private.token", "worlds_local/world.fwl"):
            with self.subTest(name=name), self.assertRaises(AssertionError):
                read_package(package([(name, b"data")]))

    def test_rejects_duplicate_entries(self):
        with self.assertRaises(AssertionError):
            read_package(package([("export.r2x", b"{}"), ("export.r2x", b"{}")]))

    def test_rejects_credentials_and_unexpected_dll(self):
        fake_credential = ("gh" + "p_" + "x" * 24).encode()
        with self.assertRaises(AssertionError):
            read_package(package([("BepInEx/config/example.cfg", fake_credential)]))
        with self.assertRaises(AssertionError):
            read_package(package([("BepInEx/plugins/Unexpected.dll", b"binary")]))


if __name__ == "__main__":
    unittest.main()
