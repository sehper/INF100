from pathlib import Path
import json
import os
directory_of_current_file = os.path.dirname(__file__)
os.chdir(directory_of_current_file)

data = json.loads(Path("cryptids.json").read_text(encoding="utf-8"))

ny_kryptid = {
    "navn": "Bybjørnen",
    "sted": "Bergen",
    "observasjoner": 3,
    "farlig": False,
    "kjennetegn": ["regnjakke", "spiser boller"]
}

data["kryptider"].append(ny_kryptid)
data["versjon"] += 1
data["sist_oppdatert"] = "2026-09-18"

content = json.dumps(data, ensure_ascii=False, indent=2)
Path("new_cryptids.json").write_text(content, encoding="utf-8")