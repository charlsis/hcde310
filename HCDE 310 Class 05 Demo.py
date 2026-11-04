# HCDE 310 Class 5: Nested JSON, then your first live API call
# All the code from today's class, for review.
# Run it with: python3 class05_demo.py
# Put aic_sample.json in the same folder first (it's in Week 3 on Canvas).
# Tip: before you run each section, predict what it will print.

import json


# ---- Tip of the day: print() with , or + ----
print("Room", 243)       # a comma prints both, with a space between: Room 243
print(2 + 3)             # + adds numbers: 5
print("a" + "b")         # + joins text: ab
# print("Room" + 243)    # TypeError: can't join text and a number. Uncomment to see it.
print()


# ---- From In-class 4: a function doesn't need return ----
def greet():
    print("hi")

x = greet()      # prints hi
print(x)         # None: without return, a function hands back None
# x.upper()      # AttributeError: None has no .upper(). Uncomment to see it.
print()


# ---- Brackets and boxes ----
tags = ["city", "night", "diner"]    # list [ ]: get one by position
art = {"title": "Nighthawks"}        # dict { }: get one by name
print(tags[0])
print(art["title"])
print(len(tags))                     # ( ) calls a function
print(f"Title: {art['title']}")      # f"...{x}..." puts a value into text
print()


# ---- Warm-up: a list inside a dict ----
art = {"title": "Nighthawks",
       "tags": ["city", "night", "diner"]}
print(art["tags"][1])
print(len(art["tags"]))
print()


# ---- Follow the path, one level at a time ----
with open("aic_sample.json") as f:   # open the file; with closes it when the block ends
    data = json.load(f)              # JSON text -> Python dicts and lists (null -> None)

results = data["data"]   # a list
first = results[0]       # a dict
print(first["title"])
print(data["data"][0]["title"])      # the same path in one line

# Stuck? type() tells you what you're holding.
print(type(data))        # <class 'dict'>
print(type(results))     # <class 'list'>
print(type(first))       # <class 'dict'>
print()


# ---- Find four fields ----
# Try it: in aic_sample.json, find the path to the total number of results,
# the second result's title, the first result's artist, and an image_id.
# Which fields are null (None in Python)?


# ---- When the data says null ----
art = data["data"][2]
print(art["artist_title"])           # None: the file says "artist_title": null
# print("By " + art["artist_title"]) # TypeError: can't join text and None. Uncomment to see it.
print("By " + (art.get("artist_title") or "Unknown artist"))
# Trap: art.get("artist_title", "Unknown artist") still gives None,
# because the key exists. .get()'s default only covers a MISSING key.
print()


# ---- The URL, piece by piece ----
# https://api.artic.edu/api/v1/artworks/search?q=cats&fields=title,artist_display,date_display,image_id
#   api.artic.edu             which server
#   /api/v1/artworks/search   which endpoint
#   ?                         parameters start here
#   q=cats                    the search term
#   &                         separates parameters
#   fields=...                which fields to send back for each artwork
# Try it: paste the URL into a browser.


# ---- requests by hand ----
# Install it first, in the terminal (at %, not at >>>):
#   python3 -m pip install requests
# If that fails, make a virtual environment in this folder:
#   python3 -m venv .venv
#   source .venv/bin/activate        (Windows: .venv\Scripts\activate)
#   python -m pip install requests
import requests

url = "https://api.artic.edu/api/v1/artworks/search"
r = requests.get(url, params={"q": "cats",
                              "fields": "title,artist_display,date_display,image_id"})
print(r.url)             # requests built the ?, & and = for you
print(r.status_code)     # 200 means it worked
if r.status_code == 200:
    data = r.json()      # the same as json.load, but for a web response
    print(data["pagination"]["total"], "results")
    for art in data["data"]:
        print(art["title"], "|", art.get("artist_display") or "Unknown artist")
else:
    print("Request failed:", r.status_code)
print()


# ---- You just used an object ----
print(type(r))           # <class 'requests.models.Response'>: r is a Response object
print(r.ok, r.reason)    # data it holds
print([name for name in dir(r) if not name.startswith("_")])   # everything it has
