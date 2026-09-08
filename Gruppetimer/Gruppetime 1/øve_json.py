import json
from pathlib import Path

path = Path(__file__).parent / "list.csv"

quotes = Path(path).read_text(encoding = "utf_8")
y = json.loads(quotes)

for quote in y["quote"]:
    print(quote[0])