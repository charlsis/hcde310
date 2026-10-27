# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
The path to the first artwork's title is data["data"][0]["title"]


## 2. Find 3 more fields you'd want to show a user, and their paths
Place of origin 2nd display is data["data"][1]["place_of_origin"]
Dimensions of 1st display is data["data"][0]["dimensions"]
Nested description of image is data["data"][0]["thumbnail"]["alt_text"]


## 3. Which fields are `null` for some works?
data["data"][2]["artist_title"]


## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
If I run it now, unchanged, it will ask me for a search term, but then it will be error when it calls the requests.get because url is an empty string and params is also empty.


## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
The error traceback mentions "requests.exceptions.MissingSchema: Invalid URL". This means an empty string is given as the URL, no web address to fetch. Line 16 of the file causes the crash, the part that calls response.