# In-class 6: NASA EPIC (photos of the whole Earth from space), with the key kept in .env
#
# 1. Load the key from .env (python-dotenv: load_dotenv(), then os.getenv("NASA_API_KEY"))
# 2. Call https://api.nasa.gov/EPIC/api/natural with your key as the api_key parameter,
#    and timeout=10 so it gives up instead of hanging if the server is slow
# 3. Check r.status_code before you use the data
# 4. The reply is a list of today's photos. Print the caption and the date of the first one

import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("NASA_API_KEY")

if key is None:
    print("No NASA_API_KEY found. Make a .env file first.")
else:
    r = requests.get("https://api.nasa.gov/EPIC/api/natural",
                     params={"api_key": key}, timeout=10)
    print(r.status_code)
    if r.status_code == 200:
        print(r.json()[0]["caption"])
        print(r.json()[0]["date"])
    else:
        print("Request failed:", r.status_code, r.reason)

def newest_photo(photos):                          # define a function that takes a list of photo dicts
    if not photos:                                 # check if the list is empty
        return None                                # nothing to compare, so return "no value"
    return max(photos, key=lambda p: p["date"])    # pick the photo whose "date" is the latest

if r.status_code == 200:                           # only continue if NASA's request succeeded
    latest = newest_photo(r.json())                # turn the response into a list, find the newest photo
    if latest:                                     # make sure we actually got a photo back (not None)
        print(latest["caption"])                   # print the newest photo's caption
        print(latest["date"])                      # print the newest photo's date