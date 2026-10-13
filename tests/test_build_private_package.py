import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import zipfile

from scripts.build_private_package import build_private
from scripts.verify_history import read_package


class PrivatePackageValidation(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        directory = Path(self.temporary.name)
        self.settings = directory / "private-admins.json"
        self.public = directory / "public.r2z"
        self.output = directory / "private.r2z"
        self.admins = [{"id": "Steam_" + digit * 17, "name": name}
                       for digit, name in (("1", 'Player "One"'), ("2", "玩家二"))]
        self.settings.write_text(json.dumps({"admins": self.admins}), encoding="utf-8")
        self.files = {
            "export.r2x": json.dumps({"profileName": "test", "mods": []}).encode(),
            "BepInEx/config/server_devcommands.cfg": b"[1. General]\nAutomatic devcommands = false\nAutomatic no cost mode = false\n",
            "BepInEx/config/other.cfg": b"[General]\nEnabled = true\n",
        }
        with zipfile.ZipFile(self.public, "w", zipfile.ZIP_DEFLATED) as archive:
            for name, data in self.files.items():
                archive.writestr(name, data)

    def test_only_admin_settings_change(self):
        original = self.public.read_bytes()
        build_private(self.settings, self.public, self.output)
        files = read_package(self.output)
        self.assertEqual(self.public.read_bytes(), original)
        self.assertEqual(files["BepInEx/config/other.cfg"], self.files["BepInEx/config/other.cfg"])
        self.assertEqual(files["export.r2x"], self.files["export.r2x"])
        server = files["BepInEx/config/server_devcommands.cfg"]
        self.assertIn(b"Automatic devcommands = true", server)
        self.assertIn(b"Automatic no cost mode = false", server)
        permissions = files["BepInEx/config/permissions.yaml"].decode()
        self.assertEqual(permissions.count('admin: "yes"'), 2)
        self.assertIn('permissions: "no"', permissions)
        for admin in self.admins:
            self.assertIn(json.dumps(admin["id"]), permissions)
            self.assertIn(json.dumps(admin["name"], ensure_ascii=False), permissions)
        self.assertNotIn("BepInEx/config/permissions.yaml", read_package(self.public))

    def test_same_inputs_produce_identical_archive(self):
        first = build_private(self.settings, self.public, self.output)
        contents = self.output.read_bytes()
        self.assertEqual(build_private(self.settings, self.public, self.output), first)
        self.assertEqual(self.output.read_bytes(), contents)

    def test_windows_utf8_bom_settings_are_accepted(self):
        self.settings.write_bytes(b"\xef\xbb\xbf" + self.settings.read_bytes())
        build_private(self.settings, self.public, self.output)
        self.assertTrue(self.output.is_file())

    def test_wrong_json_shape_has_clear_error(self):
        for settings in ([], {}):
            with self.subTest(settings=settings):
                self.settings.write_text(json.dumps(settings), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "exactly two admin accounts"):
                    build_private(self.settings, self.public, self.output)
                self.assertFalse(self.output.exists())

    def test_wrong_config_section_is_rejected(self):
        server_file = "BepInEx/config/server_devcommands.cfg"
        self.files[server_file] = self.files[server_file].replace(b"1. General", b"Wrong Section")
        with zipfile.ZipFile(self.public, "w", zipfile.ZIP_DEFLATED) as archive:
            for name, data in self.files.items():
                archive.writestr(name, data)
        with self.assertRaisesRegex(ValueError, "in 1. General"):
            build_private(self.settings, self.public, self.output)
        self.assertFalse(self.output.exists())

    def test_missing_settings_does_not_fall_back_to_public_package(self):
        self.settings.unlink()
        with self.assertRaisesRegex(FileNotFoundError, "docs/private-package.md"):
            build_private(self.settings, self.public, self.output)
        self.assertFalse(self.output.exists())

    def test_windows_line_endings_are_preserved(self):
        server_file = "BepInEx/config/server_devcommands.cfg"
        self.files[server_file] = self.files[server_file].replace(b"\n", b"\r\n")
        with zipfile.ZipFile(self.public, "w", zipfile.ZIP_DEFLATED) as archive:
            for name, data in self.files.items():
                archive.writestr(name, data)
        build_private(self.settings, self.public, self.output)
        self.assertEqual(read_package(self.output)[server_file],
                         self.files[server_file].replace(b"Automatic devcommands = false",
                                                        b"Automatic devcommands = true"))

    def test_boolean_casing_is_accepted(self):
        server_file = "BepInEx/config/server_devcommands.cfg"
        for value in (b"True", b"FALSE"):
            with self.subTest(value=value):
                files = dict(self.files)
                files[server_file] = files[server_file].replace(b"Automatic devcommands = false",
                                                              b"Automatic devcommands = " + value)
                with zipfile.ZipFile(self.public, "w", zipfile.ZIP_DEFLATED) as archive:
                    for name, data in files.items():
                        archive.writestr(name, data)
                build_private(self.settings, self.public, self.output)
                self.assertEqual(read_package(self.output)[server_file],
                                 self.files[server_file].replace(b"Automatic devcommands = false",
                                                                b"Automatic devcommands = true"))

    def test_invalid_or_duplicate_id_does_not_replace_existing_output(self):
        self.output.write_bytes(b"existing private delivery")
        for admins in ([{"id": "Everyone", "name": "bad"}, self.admins[1]],
                       [self.admins[0], self.admins[0]]):
            with self.subTest(admins=admins):
                self.settings.write_text(json.dumps({"admins": admins}), encoding="utf-8")
                with self.assertRaises(ValueError):
                    build_private(self.settings, self.public, self.output)
                self.assertEqual(self.output.read_bytes(), b"existing private delivery")


if __name__ == "__main__":
    unittest.main()
