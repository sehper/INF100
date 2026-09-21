from pathlib import Path
import json
import os
directory_of_current_file = os.path.dirname(__file__)
os.chdir(directory_of_current_file)

content = Path("cryptids_fixed.json").read_text(encoding="utf-8")
data = json.loads(content)

print(data["kryptider"][-1]["navn"])
print()

for i, kryptid in enumerate(data["kryptider"], start=1):
    print(f"{i}. {kryptid['navn']}: {kryptid['kjennetegn']}")
print()

for key, value in data["kryptider"][0].items():
    print(f"{key} : {value}")

total = 0
for kryptid in data["kryptider"]:
    total = total + kryptid["observasjoner"]