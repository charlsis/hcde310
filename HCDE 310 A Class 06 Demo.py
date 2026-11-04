# HCDE 310 Class 6: Modules, virtual environments, and API keys
# All the code from today's class, for review.
# Run it with: python3 class06_demo.py  (with your venv on)
# Needs: pip install requests python-dotenv
# Tip: before you run each section, predict what it will print.

import json        # comes with Python: in every toolbox
import os          # comes with Python too
import requests    # you added this one with pip install


# ---- Review: one API call, start to finish ----
#   https://api.artic.edu/api/v1   /artworks   ?limit=3
#           base URL               endpoint    parameters
url = "https://api.artic.edu/api/v1/artworks"
r = requests.get(url, params={"limit": 3})   # call the API, save the reply in r

print(type(r))        # <class 'requests.models.Response'>: the response object, the "envelope"
data = r.json()       # turn the reply's text into a Python dict
print(type(data))     # <class 'dict'>
art = data["data"]    # the list of artworks
print(type(art))      # <class 'list'>
print(art[0]["title"])  # one field from one artwork
print()


# ---- What's in the response object ----
# No ( ): an attribute, something r already has
# With ( ): a method, asking r to do something
print(r.status_code)  # 200: the number, did it work?
print(r.reason)       # OK: the name for that number
print(r.text[:60])    # the reply as raw text (one long string), first 60 characters
print(r.url)          # the URL that was actually requested, parameters included
print(list(r.json().keys()))   # ['pagination', 'data', 'info', 'config']
print()


# ---- Status codes: check before you use the data ----
# 2xx worked, 3xx go somewhere else, 4xx you made a mistake, 5xx the server had a problem
r = requests.get("https://api.artic.edu/api/v1/artworks/99999999")   # an id that doesn't exist
if r.status_code == 200:
    print(r.json()["data"]["title"])
elif r.status_code == 404:
    print("We couldn't find that artwork. Check the ID, or try a search.")
else:
    print("Something went wrong:", r.status_code, r.reason)
print()


# ---- Warm-up: brand-new project. Which lines work? ----
# import json        works: comes with Python
# import requests    fails in a fresh venv until you pip install it there
# import pandas      fails: never installed
# (ModuleNotFoundError means "that tool isn't in this toolbox")


# ---- Virtual environments: this project's toolbox ----
# Type these in the terminal (at %), not in Python (at >>>):
#   python3 -m venv .venv                 make the toolbox (once, in your hcde310 folder)
#   source .venv/bin/activate             open it (Mac)
#   .venv\Scripts\activate                open it (Windows, no "source")
#   pip install requests                  add a tool to this box
#   pip show requests                     version, Location: (inside .venv), Requires:
#   pip freeze                            list every tool in the box
#   deactivate                            close it
# (.venv) in your prompt means it's open.
# requests brought 4 tools of its own: certifi, charset-normalizer, idna, urllib3.


# ---- Where libraries live ----
print(json.__file__)       # inside Python's own folder
print(requests.__file__)   # inside .venv/.../site-packages
print(requests.__version__)
print()


# ---- What's odd? Compare the totals ----
base = "https://api.artic.edu/api/v1/artworks"
for path in ["?limit=1", "/search?q=cats&limit=1", "/search?q=zzzqqxx&limit=1"]:
    r = requests.get(base + path)
    print(path, r.json()["pagination"]["total"])
# All three print the same total. The q= search ranks every artwork, it doesn't filter.
# The docs don't say this: we found it by testing. A real count searches one field:
r = requests.get(base + "/search", params={"query[match][title]": "cats", "limit": 1})
print("title has 'cats':", r.json()["pagination"]["total"])
print()


# ---- API keys: keep the secret out of your code ----
# 1. Get a free key at api.nasa.gov
# 2. Make a file named .env next to this one, with one line:  NASA_API_KEY=your_key_here
# 3. Make sure .env is in your .gitignore (it never gets committed)
from dotenv import load_dotenv

load_dotenv()                        # reads .env into environment variables
key = os.getenv("NASA_API_KEY")      # the code asks for the key, it doesn't contain it
if key is None:
    print("No NASA_API_KEY found. Make a .env file first (steps above).")
else:
    r = requests.get("https://api.nasa.gov/EPIC/api/natural",
                     params={"api_key": key}, timeout=10)   # give up after 10 s instead of hanging
    if r.status_code == 200:
        print(r.json()[0]["caption"])   # today's first photo of the whole Earth
    else:
        print("Request failed:", r.status_code, r.reason)   # 403 = bad or missing key
