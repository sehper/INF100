import json
from datetime import datetime, timezone
import requests
 
URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.39&lon=5.32"
# Bytt ut <uib-brukernavn> med ditt eget UiB-brukernavn.
HEADERS = {"User-Agent": "inf100.ii.uib.no nilun6880"}
 
 
def weather_in_bergen_next_hour():
    """Returnerer symbol_code for været i Bergen den nærmeste timen."""
    response = requests.get(URL, headers=HEADERS)
    d = json.loads(response.text)
 
    timeseries = d["properties"]["timeseries"]
    now = datetime.now(timezone.utc)
 
    def avstand(entry):
        t = datetime.fromisoformat(entry["time"].replace("Z", "+00:00"))
        return abs((t - now).total_seconds())
 
    closest = min(timeseries, key=avstand)
 
    data = closest["data"]
    if "next_1_hours" in data:
        return data["next_1_hours"]["summary"]["symbol_code"]
    return data["next_6_hours"]["summary"]["symbol_code"]
 
 
if __name__ == "__main__":
    print("Været i Bergen neste time:", weather_in_bergen_next_hour())