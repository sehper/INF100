from pathlib import Path
import json

path = Path(__file__).parent / "kontakter.json"

x = Path(path).read_text(encoding= "utf-8" )
y = json.loads(x)

for contacts in y["contacts"]:
    print(contacts["name"])
