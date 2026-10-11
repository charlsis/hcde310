# HCDE 310 Class 3: Decisions and dictionaries
# All the code from today's class, for review.
# Run it with: python3 class03_demo.py
# Tip: before you run each section, predict what it will print.


# ---- Warm-up ----
years = [1889, 1942, 1930, 1973]
for y in years:
    if y > 1900:
        print(y, "modern")
# How many lines printed? Why not 4?
print()


# ---- Conditionals ----
year = 1942
if year < 1900:
    print("old")
elif year < 1950:
    print("mid-century")
else:
    print("recent")
# Only the first True branch runs. Try it: change year to 1889, then 2001.
# Comparisons: < > <= >= == !=      Combine: and, or, not
# = stores a value. == asks a question:
print(year == 1942)
print()


# ---- Sequence, decision, iteration ----
years = [1889, 1942, 1930, 1973]   # sequence: lines run top to bottom
for y in years:                    # iteration: repeat lines
    if y > 1900:                   # decision: choose which lines run
        print(y, "modern")
print()


# ---- Your Day 1 app: what if nothing matches? ----
results = []   # pretend the search found nothing
if len(results) == 0:
    print("No results.")
else:
    for r in results:
        print(r)
# Try it: put "Nighthawks" in the list and run again.
print()


# ---- Dictionaries ----
# A dictionary stores key-value pairs: look up a value by its key, not its position.
phone = {"Ana": "555-1234", "Sam": "555-9876"}
print(phone["Ana"])
print()


# ---- One artwork as a dictionary ----
art = {"title": "The Bedroom",
       "artist": "Vincent van Gogh",
       "year": 1889}
print(art["title"])
print(art.get("medium", "Unknown"))   # .get gives a fallback instead of crashing
# Try it: remove the # below and run again. The key isn't there, so you get a KeyError.
# print(art["medium"])
print()


# ---- A list of dictionaries: many artworks ----
# This is how most API data looks (Week 3).
artworks = [
    {"title": "The Bedroom", "artist": "Vincent van Gogh"},
    {"title": "Nighthawks", "artist": "Edward Hopper"},
]
for art in artworks:
    print(art["title"], "–", art["artist"])
print()


# ---- Parallel lists (Class 2) vs. a list of dictionaries ----
titles = ["The Bedroom", "Nighthawks", "Mao"]
years = [1889, 1942, 1973]
for i in range(len(titles)):
    print(titles[i], years[i])
print()

artworks = [
    {"title": "The Bedroom", "artist": "Vincent van Gogh", "year": 1889},
    {"title": "Nighthawks", "artist": "Edward Hopper", "year": 1942},
    {"title": "Mao", "artist": "Andy Warhol", "year": 1973},
]
for a in artworks:
    print(a["title"], a["year"])
# Same output. Each artwork's facts now travel together, so they can't get out of step.
print()


# ---- Data is a design decision: three ways to model a visit planner ----
# 1. Favorites on each artwork: simple, but a second visitor breaks it
artworks = [
    {"title": "The Bedroom", "gallery": "Gallery 2", "favorite": True},
    {"title": "Mao", "gallery": "Gallery 5", "favorite": False},
]

# 2. Separate lists, linked by ID: each artwork stored once; loop to find "a3"
artworks = [
    {"id": "a1", "title": "The Bedroom", "gallery": "Gallery 2"},
    {"id": "a2", "title": "Nighthawks", "gallery": "Gallery 4"},
    {"id": "a3", "title": "Mao", "gallery": "Gallery 5"},
]
visitors = [{"name": "visitor1", "favorites": ["a1", "a3"]}]
for a in artworks:
    if a["id"] == "a3":
        print(a["title"])

# 3. A dictionary keyed by ID: a second visitor is one new line, no loop
artworks = {
    "a1": {"title": "The Bedroom", "gallery": "Gallery 2"},
    "a2": {"title": "Nighthawks", "gallery": "Gallery 4"},
    "a3": {"title": "Mao", "gallery": "Gallery 5"},
}
visitors = {"visitor1": {"favorites": ["a1", "a3"]}}
visitors["visitor2"] = {"favorites": ["a2", "a3"]}
print(artworks["a3"]["title"])
print(visitors)
print()


# ---- Adding and changing keys ----
counts = {}          # create an empty dictionary
counts["b"] = 1      # adds a new key
counts["a"] = 1
counts["n"] = 1
counts["a"] = 2      # updates "a", doesn't add a second one
print(counts)
print()


# ---- Counting with a dictionary ----
counts = {}
for letter in "banana":
    if letter in counts:          # is the key there yet?
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1
print(counts)
print()


# ---- A shortcut: .get with a default ----
# counts.get(letter, 0) means "the current count, or 0 if it's new." It replaces the if/else.
counts = {}
for letter in "banana":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)
# The pattern: counts[key] = counts.get(key, 0) + 1
# Try it: count the letters in your own name.


# --- In Class Activity ---

# dictionary in a list
museum = [
    {"artwork": {"title": "The Bedroom", "artist": "Vincent van Gogh", "year": "1889"},
          "gallery": 2, "favorite": True},
    {"artwork": {"title": "Nighthawks", "artist": "Edward Hopper", "year": "1942"},
        "gallery": 4, "favorite": False}
]

for art in museum:
    print(art["artwork"]["title"], art["favorite"])