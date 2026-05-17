import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SERPAPI_API_KEY")

params = {
    "api_key": API_KEY,
    "engine": "google_flights",
    "departure_id": "JFK",
    "arrival_id": "AUS",
    "outbound_date" : "2026-06-20",
    "return_date" : "2026-08-20",
}
print(f"Key loaded:{API_KEY}")
search = requests.get("https://serpapi.com/search", params=params)
results = search.json()
# print(json.dumps(results, indent=2))

keys = ["best_flight","other_flights"]

for key in keys:
    print("Key:",key)
    if key not in results:
        continue
    for item in results[key]:

        for flight in item["flights"]:
            print(flight["departure_airport"]["name"], flight["departure_airport"]["time"])
            print(flight["arrival_airport"]["name"], flight["arrival_airport"]["time"])
            print("Airplane:" + flight["airplane"] + " " + flight["airplane"])
        print("Price:" + str(item["price"]))
        print("Departure token: " + str(item["departure_token"]))
        print("")
