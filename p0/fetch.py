import requests
import json

headers = {"User-Agent": "MyP0App (charlsis@uw.edu)"}

# ---------- Resource 1: Open-Meteo Air Quality (Pekanbaru, Riau) ----------
url1 = "https://air-quality-api.open-meteo.com/v1/air-quality"
params1 = {
    "latitude": 0.51,
    "longitude": 101.45,
    "current": "pm2_5,us_aqi",
}
response1 = requests.get(url1, params=params1, headers=headers)
print("URL 1:", response1.url)                      # the full URL, for p0.md
print(json.dumps(response1.json(), indent=2))       # indent=2 makes it easy to read

# ---------- Resource 2: TheMealDB (recipes) ----------
url2 = "https://www.themealdb.com/api/json/v1/1/filter.php"   # the "1" is the test key
params2 = {
    "i": "salmon",            # i = main ingredient
}
response2 = requests.get(url2, params=params2, headers=headers)
print("URL 2:", response2.url)

data2 = response2.json()
first_two = {"meals": data2["meals"][:2]}   # keep just the first 2 meals
print(json.dumps(first_two, indent=2))