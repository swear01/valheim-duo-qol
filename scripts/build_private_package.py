"""Apply the local two-player admin settings to the verified public package."""
import configparser
import json
from pathlib import Path
import re
import tempfile
import zipfile

from scripts import build_package
from scripts.verify_history import ROOT, digest, read_package

PRIVATE_SETTINGS = Path.home() / ".config/valheim-duo-qol/private-admins.json"


def load_admins(path):
    try:
        text = path.read_text(encoding="utf-8-sig")
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Missing private admin settings: {path}. Restore this file; see docs/private-package.md"
        ) from None
    settings = json.loads(text)
    admins = settings.get("admins") if isinstance(settings, dict) else None
    if not isinstance(admins, list) or len(admins) != 2:
        raise ValueError("Private settings must contain exactly two admin accounts")
    for admin in admins:
        if not isinstance(admin, dict) or not re.fullmatch(r"Steam_\d{17}", str(admin.get("id", ""))):
            raise ValueError("Each admin requires a complete Steam account ID")
        if not isinstance(admin.get("name"), str) or not admin["name"].strip():
            raise ValueError("Each admin requires a display name")
    if len({admin["id"] for admin in admins}) != 2:
        raise ValueError("Private admin accounts must be distinct")
    return admins


def build_private(settings_path, public_archive, output):
    admins = load_admins(settings_path)
    if public_archive.resolve() == output.resolve():
        raise ValueError("Private output must differ from the public archive")
    files = read_package(public_archive)
    permission_file = "BepInEx/config/permissions.yaml"
    if permission_file in files:
        raise ValueError("Public archive already contains permissions; inspect before replacing")
    server_file = "BepInEx/config/server_devcommands.cfg"
    text = files[server_file].decode("utf-8-sig")
    parser = configparser.ConfigParser(interpolation=None)
    parser.optionxform = str
    parser.read_string(text)
    try:
        parser.getboolean("1. General", "Automatic devcommands")
    except (configparser.Error, ValueError):
        raise ValueError("Automatic devcommands setting is missing or invalid in 1. General") from None
    pattern = r"(?mi)^(Automatic devcommands[ \t]*=[ \t]*)(?:true|false)([ \t]*\r?)$"
    if len(re.findall(pattern, text)) != 1:
        raise ValueError("Automatic devcommands setting is missing or ambiguous")
    files[server_file] = re.sub(pattern, r"\g<1>true\g<2>", text).encode("utf-8")
    permissions = '- name: Everyone\n  commands:\n    permissions: "no"\n'
    for admin in admins:
        permissions += "\n- id: " + json.dumps(admin["id"]) + "\n"
        permissions += "  name: " + json.dumps(admin["name"], ensure_ascii=False) + '\n  admin: "yes"\n'
    files[permission_file] = permissions.encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=output.parent, delete=False) as temporary:
        pending = Path(temporary.name)
    try:
        with zipfile.ZipFile(public_archive) as template, zipfile.ZipFile(pending, "w") as archive:
            archive.comment = template.comment
            for info in template.infolist():
                archive.writestr(info, files[info.filename])
            info = zipfile.ZipInfo(permission_file, template.getinfo("export.r2x").date_time)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, files[permission_file])
        if read_package(pending) != files:
            raise ValueError("Private package contents differ")
        pending.replace(output)
    finally:
        pending.unlink(missing_ok=True)
    return digest(output.read_bytes())


def main():
    load_admins(PRIVATE_SETTINGS)
    build_package.main()
    row = json.loads((ROOT / "history/versions.json").read_text(encoding="utf-8"))[-1]
    public = ROOT / "dist" / Path(row["archive"]).name
    output = public.parent / "private" / public.name
    checksum = build_private(PRIVATE_SETTINGS, public, output)
    print(f"PASS: {output.relative_to(ROOT)}; two private admins; SHA256 {checksum}")


if __name__ == "__main__":
    main()
