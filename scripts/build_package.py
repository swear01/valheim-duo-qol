"""Rebuild the current Gale package from profile/ with preserved ZIP metadata."""
import json
import zipfile

from scripts.verify_history import ROOT, digest, git, read_package


def main():
    if not __debug__:
        raise RuntimeError("Package verification requires Python without -O or PYTHONOPTIMIZE")
    row = json.loads((ROOT / "history/versions.json").read_text(encoding="utf-8"))[-1]
    preserved = ROOT / row["archive"]
    files = {
        name.removeprefix("profile/"): (ROOT / name).read_bytes()
        for name in git("ls-files", "-z", "--", "profile").decode().split("\0") if name
    }
    if files != read_package(preserved):
        raise ValueError("Profile differs from preserved release")
    output = ROOT / "dist" / preserved.name
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(preserved) as template, zipfile.ZipFile(output, "w") as archive:
        archive.comment = template.comment
        for info in template.infolist():
            archive.writestr(info, files[info.filename])
    if read_package(output) != files:
        raise ValueError("Rebuilt package contents differ")
    if digest(output.read_bytes()) != row["archive_sha256"]:
        raise ValueError("Rebuilt package hash differs")
    print(f"PASS: {output.name} rebuilt from profile/; SHA256 {row['archive_sha256']}")


if __name__ == "__main__":
    main()
