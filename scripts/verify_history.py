"""Verify preserved packages, locks, source snapshots and version tags with stdlib only."""
from pathlib import Path, PurePosixPath
import configparser
import hashlib
import io
import json
import re
import subprocess
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parent.parent
SENSITIVE = re.compile(
    r"(?:/" + r"Users/|/" + r"home/)[^\s<>]+|"
    r"\b(?:gh[pousr]_|github_pat_|sk-)[A-Za-z0-9_-]{12,}|"
    r"-----BEGIN [^-]*PRIVATE KEY-----|\bBearer\s+[A-Za-z0-9._~-]{12,}"
)
BUNDLED_DLLS = {
    "BepInEx/plugins/aedenthorn-TorchMod/TorchMod.dll",
    "BepInEx/plugins/swear-AAACraftingMaxFix/AAACraftingMaxFix.dll",
    "BepInEx/plugins/swear-SlashBackFix/SlashBackFix.dll",
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def release_bytes(tag, name):
    path = ROOT / name
    if path.exists():
        return path.read_bytes()
    return git("show", f"{tag}:{name}")


def check_text(data, label):
    text = data.decode("utf-8-sig")
    assert not SENSITIVE.search(text), f"Private data in {label}"


def read_package(path):
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, path
        names = archive.namelist()
        assert len(names) == len(set(names)), path
        files = {}
        for name in names:
            member = PurePosixPath(name)
            assert not member.is_absolute() and ".." not in member.parts and "\\" not in name, name
            assert name == "export.r2x" or name.startswith(("BepInEx/config/", "BepInEx/plugins/")), name
            assert not any("token" in part.lower() for part in member.parts), name
            data = archive.read(name)
            if name.endswith(".dll"):
                assert name in BUNDLED_DLLS, name
            else:
                check_text(data, name)
            files[name] = data
        return files


def tag_profile(tag):
    raw = git("archive", "--format=tar", tag, "profile")
    with tarfile.open(fileobj=io.BytesIO(raw)) as archive:
        return {
            member.name.removeprefix("profile/"): archive.extractfile(member).read()
            for member in archive.getmembers() if member.isfile()
        }


def main():
    history = json.loads((ROOT / "history/versions.json").read_text())
    assert history and [r["version"] for r in history] == list(range(1, len(history) + 1))
    if not (ROOT / history[-1]["archive"]).is_file():
        raise FileNotFoundError("Latest package must remain in the checkout")
    prior_tag = None
    last_files = None
    for row in history:
        tag = row["tag"]
        assert tag == f"v{row['version']}"
        path = ROOT / row["archive"]
        archive_bytes = release_bytes(tag, row["archive"])
        assert digest(archive_bytes) == row["archive_sha256"], tag
        assert len(archive_bytes) == row["archive_bytes"], tag
        files = read_package(io.BytesIO(archive_bytes))
        assert {n: digest(b) for n, b in files.items()} == row["entries_sha256"], tag
        lock_bytes = release_bytes(tag, row["lock"])
        assert digest(lock_bytes) == row["lock_sha256"], tag
        check_text(lock_bytes, row["lock"])
        lock = json.loads(lock_bytes)
        export = json.loads(files["export.r2x"])
        assert export["profileName"] == row["profile"] == lock["profile"], tag
        assert lock["created"] == row["release_date"], tag
        packages = {p["name"]: p for p in lock["packages"]}
        assert len(packages) == len(export["mods"]) == row["online_packages"], tag
        assert len({m["name"] for m in export["mods"]}) == len(packages), tag
        for mod in export["mods"]:
            package = packages[mod["name"]]
            assert mod["enabled"] and mod["source"] == package["source"], tag
            version = ".".join(str(mod["version"][k]) for k in ("major", "minor", "patch"))
            assert version == package["version"], tag
            for requirement in package["dependencies"]:
                name, minimum = requirement.rsplit("-", 1)
                assert name in packages, (tag, requirement)
                assert tuple(map(int, packages[name]["version"].split("."))) >= tuple(map(int, minimum.split("."))), (tag, requirement)
        configs = {n: b for n, b in files.items() if n.startswith("BepInEx/config/")}
        assert len(configs) == row["configuration_files"], tag
        for config in lock["configs"].values():
            if config.get("format") == "yaml":
                assert "BepInEx/config/" + config["filename"] in configs
                continue
            parser = configparser.ConfigParser(interpolation=None)
            parser.optionxform = str
            parser.read_string(configs["BepInEx/config/" + config["filename"]].decode("utf-8-sig"))
            for section, values in config["sections"].items():
                for key, value in values.items():
                    assert parser[section][key] == str(value), (tag, config["filename"], section, key)
        recorded = lock.get("artifacts_sha256", {}).get(path.name)
        if recorded:
            assert recorded == row["archive_sha256"], tag
            assert row["archive_hash_evidence"] == "matches_original_lock"
        else:
            assert row["version"] <= 6
            assert row["archive_hash_evidence"] == "computed_on_import_original_lock_had_no_archive_digest"
        assert tag_profile(tag) == files, f"Tag snapshot differs: {tag}"
        assert git("show", f"{tag}:lock.json") == lock_bytes, tag
        tag_history = json.loads(git("show", f"{tag}:history/versions.json"))
        assert len(tag_history) == row["version"] and tag_history[-1]["archive_sha256"] == row["archive_sha256"], tag
        if prior_tag:
            subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", prior_tag, tag], check=True)
        prior_tag, last_files = tag, files
    current = {p.relative_to(ROOT / "profile").as_posix(): p.read_bytes() for p in (ROOT / "profile").rglob("*") if p.is_file()}
    assert current == last_files, "Current profile differs from latest preserved package"
    assert (ROOT / "lock.json").read_bytes() == (ROOT / history[-1]["lock"]).read_bytes()
    tracked = git("ls-files", "-z").decode().split("\0")[:-1]
    for name in tracked:
        path = ROOT / name
        if path.suffix not in {".r2z", ".dll"}:
            check_text(path.read_bytes(), name)
    for name in ("README.md", "CHANGELOG.md", "docs/history.md", "THIRD_PARTY.md"):
        path = ROOT / name
        for href in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if not href.startswith(("https://", "http://", "#")):
                assert (path.parent / href.split("#", 1)[0]).exists(), (name, href)
    print(f"PASS: {len(history)} original archives/locks, all version tags, pins/dependencies/configs, exact profile snapshots, public-data scan and documentation links.")


if __name__ == "__main__":
    main()
