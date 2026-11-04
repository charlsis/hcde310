# HCDE 310 Class 7: input(), debugging in VS Code, and a first look at Flask
# All the code from today's class, for review.
# Run it with: python3 class07_demo.py
# Tip: before you run each section, predict what it will print.


# ---- Warm-up: input() ----
# The program pauses and waits for you to type. Whatever you type comes back as a string.
term = input("Search for: ")
print("You searched for", term)
print(type(term))     # <class 'str'>, even if you typed 5 ("5", not 5)
print()


# ---- Debugging 1: newest_photo, from the pairs activity (no error, just a wrong answer) ----
# Sample photos with the same shape as earth.py's photos (no key or internet needed)
photos = [
    {"caption": "Earth from 1 million miles", "date": "2026-10-19 00:31:45"},
    {"caption": "Earth from 1 million miles", "date": "2026-10-19 13:43:04"},
    {"caption": "Earth from 1 million miles", "date": "2026-10-19 06:12:57"},
]

# AI-written
def newest_photo(photos): # there's a bug in this code! how do we find out? (vscode debugger)
    """Takes a list of photos and returns the one with the latest date."""
    newest = photos[0]
    for photo in photos:
        if photo["date"] > newest["date"]:
            newest = photo
        return newest          

print("Buggy:", newest_photo(photos)["date"])  
# Predict first: which date should it print? Then run it. No error, just the wrong answer.
#
# Debug it in VS Code instead of adding prints:
# 1. Click just right of the line number of the "if" line: a red dot (a breakpoint).
# 2. Run button's ▾ menu → "Python Debugger: Debug Python File".
# 3. It pauses at the red dot. The Variables panel shows photo and newest right now.
# 4. Press Continue (leftmost on the debug toolbar). Expected: it stops at the "if"
#    again for the second photo. It doesn't: the function already returned.
#    That's the clue: the return runs on the first time through the loop.

def newest_photo(photos):
    """Takes a list of photos and returns the one with the latest date."""
    newest = photos[0]
    for photo in photos:
        if photo["date"] > newest["date"]:
            newest = photo
    return newest              # fixed: after the loop, once every photo has been checked

print("Fixed:", newest_photo(photos)["date"])          # 13:43:04
# Why does > work on dates? They're strings, but "2026-10-19 13:..." sorts like a date
# because the biggest unit (year) comes first.
print()


# ---- Debugging 2: a loop that breaks on the third item (an error this time) ----
artworks = [
    {"title": "Water Lilies", "artist": "Monet"},
    {"title": "Nighthawks", "artist": "Hopper"},
    {"title": "The Bedroom"},                      # no "artist" key
]

# Try it: swap the two print lines below (comment one, uncomment the other) and run.
# The broken one crashes on the third artwork: KeyError: 'artist'
for art in artworks:
    # print(art["title"], "by", art["artist"])                     # breaks on the third one
    print(art["title"], "by", art.get("artist", "unknown artist"))  # .get gives a default instead
print()

# Debug it in VS Code instead of adding prints:
# 1. Click just right of the line number of the print line: a red dot (a breakpoint).
# 2. Run button's ▾ menu → "Python Debugger: Debug Python File".
# 3. The program pauses at the red dot. The Variables panel shows art right now.
# 4. Press Continue (leftmost on the debug toolbar): it runs to the next stop.
#    With the broken line, the debugger also stops on the crash itself,
#    with every variable still visible.
#
# Breakpoint never stops? Look for a syntax error (a missing colon or bracket)
# anywhere in the file. Python reads the whole file first, so one syntax error
# means nothing runs at all, not even line 1. Fix the red squiggles first.
# Guide: "Getting started with VS Code" → Debugging code (Canvas, Reference module)


# ---- Flask demo: what we built (watch first; you'll build it in Class 9 and HW4) ----
# Flask runs differently from this file: it keeps running and waits for visits.
# To try it, make a new folder with one file, app.py:
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Home page"
#
# @app.route("/about")
# def about():
#     return "About us"
#
# Then, in the terminal, with (.venv) on:
#   pip install flask
#   flask --app app run --debug
# Open http://127.0.0.1:5000, then http://127.0.0.1:5000/about. Ctrl+C stops it.
# Try http://127.0.0.1:5000/contact too: no route matches, so you get 404 Not Found.
# Mac says port 5000 is in use? Add --port 5001.
# Real pages (HTML templates) come in Class 9.
