"""Check every community lobby before it can be merged.

    python tools/validate.py              # all lobbies
    python tools/validate.py my-lobby     # just one

Standard library only, so it runs the same on your machine and in GitHub Actions.
The farmbot host runs these same rules again when it loads a lobby - passing here is
necessary, not sufficient.
"""
import fnmatch
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOBBIES = os.path.join(ROOT, "lobbies")

MODES = {"ffa", "24p", "teams", "vanilla"}
TOP_KEYS = {"$schema", "name", "author", "description", "base", "settings", "maps"}
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]{1,30}[a-z0-9]$")

# Every Duck Game level saved by the editor starts with these 8 bytes (checked across
# the 352 maps the pond runs today).
LEV_MAGIC = bytes.fromhex("59a2c8f959e21100")
MAX_MAP_BYTES = 1_000_000
MAX_MAPS = 100
MAX_PREVIEW_BYTES = 500_000
ALLOWED_EXTRA = {"README.md", "preview.png"}
MAP_PERCENTS = ["CustomMapsPercent", "NormalMapsPercent", "RandomMapsPercent", "InternetMapsPercent"]


def load_allowlist():
    allow = json.load(open(os.path.join(ROOT, "allowlist.json"), encoding="utf-8"))
    return {k: spec for c in allow["categories"] for k, spec in c["settings"].items()}


def check_value(key, spec, value, errors):
    t = spec["type"]
    if t == "bool":
        if not isinstance(value, bool):
            errors.append(f"{key} must be true or false")
    elif t in ("int", "double"):
        ok = isinstance(value, int) and not isinstance(value, bool)
        if t == "double":
            ok = ok or isinstance(value, float)
        if not ok:
            errors.append(f"{key} must be a {'whole ' if t == 'int' else ''}number")
        elif not spec["min"] <= value <= spec["max"]:
            errors.append(f"{key} = {value} is outside {spec['min']} - {spec['max']}")
    elif t == "string":
        if not isinstance(value, str):
            errors.append(f"{key} must be text")
        elif len(value) > spec["maxLength"]:
            errors.append(f"{key} is longer than {spec['maxLength']} characters")
        elif "\n" in value or "\r" in value:
            errors.append(f"{key} must be one line")
    elif t == "priceMap":
        if not isinstance(value, dict):
            errors.append(f"{key} must be an object of item -> price")
        else:
            for item, price in value.items():
                if not isinstance(price, int) or isinstance(price, bool) or not spec["min"] <= price <= spec["max"]:
                    errors.append(f"{key}.{item} must be a whole number {spec['min']} - {spec['max']}")


def check_lobby(folder, allow, seen_names):
    errors = []
    path = os.path.join(LOBBIES, folder)

    if not SLUG.match(folder):
        errors.append("folder name must be 3-32 chars of a-z, 0-9 and '-' (it becomes the @mode word)")

    lobby_file = os.path.join(path, "lobby.json")
    if not os.path.isfile(lobby_file):
        return errors + ["missing lobby.json"]

    try:
        lobby = json.load(open(lobby_file, encoding="utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        return errors + [f"lobby.json is not valid JSON: {e}"]

    if not isinstance(lobby, dict):
        return errors + ["lobby.json must be an object"]

    for k in lobby:
        if k not in TOP_KEYS:
            errors.append(f"unknown top-level field '{k}'")

    for k, n in (("name", 32), ("author", 32), ("description", 140)):
        v = lobby.get(k)
        if not isinstance(v, str) or not v.strip():
            errors.append(f"'{k}' is required")
        elif len(v) > n:
            errors.append(f"'{k}' is longer than {n} characters")

    name = (lobby.get("name") or "").strip().lower()
    if name:
        if name in seen_names:
            errors.append(f"another lobby is already called '{lobby['name']}'")
        seen_names.add(name)

    if lobby.get("base") not in MODES:
        errors.append(f"'base' must be one of {sorted(MODES)}")

    settings = lobby.get("settings", {})
    if not isinstance(settings, dict):
        errors.append("'settings' must be an object")
        settings = {}

    for key, value in settings.items():
        spec = allow.get(key)
        if spec is None:
            errors.append(f"'{key}' can't be changed by a lobby (see docs/settings.md)")
        else:
            check_value(key, spec, value, errors)

    given = [k for k in MAP_PERCENTS if k in settings]
    if given:
        if len(given) != len(MAP_PERCENTS):
            errors.append("set all four map percentages or none: " + ", ".join(MAP_PERCENTS))
        elif all(isinstance(settings[k], int) for k in MAP_PERCENTS) and sum(settings[k] for k in MAP_PERCENTS) != 100:
            errors.append("the four map percentages must add up to 100")

    for lo, hi in (
        ("CarePackageMinSeconds", "CarePackageMaxSeconds"),
        ("BettingMinBet", "BettingMaxBet"),
        ("AfkWarnRounds", "AfkKickRounds"),
        ("MinimumPlayers", "MaximumPlayers"),
    ):
        a, b = settings.get(lo), settings.get(hi)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and a > b:
            errors.append(f"{lo} ({a}) can't be more than {hi} ({b})")

    # files: lobby.json, README.md, preview.png and maps/*.lev - nothing else
    map_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        rel_dir = os.path.relpath(dirpath, path).replace(os.sep, "/")
        for f in filenames:
            rel = f if rel_dir == "." else f"{rel_dir}/{f}"
            full = os.path.join(dirpath, f)
            if rel == "lobby.json":
                continue
            if rel in ALLOWED_EXTRA:
                if rel == "preview.png" and os.path.getsize(full) > MAX_PREVIEW_BYTES:
                    errors.append("preview.png is over 500 KB")
                continue
            if rel_dir == "maps" and f.lower().endswith(".lev"):
                size = os.path.getsize(full)
                if size > MAX_MAP_BYTES:
                    errors.append(f"{rel} is over 1 MB")
                with open(full, "rb") as fh:
                    if fh.read(len(LEV_MAGIC)) != LEV_MAGIC:
                        errors.append(f"{rel} isn't a Duck Game level saved by the editor")
                map_files.append(rel)
                continue
            errors.append(f"unexpected file {rel} (allowed: lobby.json, README.md, preview.png, maps/*.lev)")

    if len(map_files) > MAX_MAPS:
        errors.append(f"{len(map_files)} maps - the limit is {MAX_MAPS}")

    patterns = lobby.get("maps", [])
    if not isinstance(patterns, list) or not all(isinstance(p, str) for p in patterns):
        errors.append("'maps' must be a list of paths like \"maps/*.lev\"")
    else:
        for p in patterns:
            if not p.startswith("maps/") or ".." in p:
                errors.append(f"map path '{p}' must be inside this lobby's maps/ folder")
            elif not fnmatch.filter(map_files, p):
                errors.append(f"map path '{p}' matches no file in maps/")

    return errors


def main():
    allow = load_allowlist()
    only = sys.argv[1:]
    folders = sorted(
        f for f in os.listdir(LOBBIES) if os.path.isdir(os.path.join(LOBBIES, f))
    ) if os.path.isdir(LOBBIES) else []

    failed = 0
    seen = set()
    for folder in folders:
        errors = check_lobby(folder, allow, seen)
        if only and folder not in only:
            continue
        if errors:
            failed += 1
            print(f"FAIL lobbies/{folder}")
            for e in errors:
                print(f"     - {e}")
        else:
            print(f"ok   lobbies/{folder}")

    if not folders:
        print("no lobbies yet")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
