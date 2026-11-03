# app.py: routes for my art search app.
# Who it's for: art students looking up artworks from the Art Institute of Chicago.

# Import Flask tools (Flask, render_template, request)
from flask import Flask, render_template, request
# Import my search_art function from api.py
# from api import search_art

# Create the app
app = Flask(__name__)

# ---------- / (home) ----------
# Show home.html, which has the search form.
@app.route("/")
def home():
   return render_template("home.html")
# (If /results sends the user back with a message, home.html shows it.)


# ---------- /results ----------
# 1. Read the search word the user typed in the form
# 2. Empty input? → back to home.html with "Please type a search word."
# 3. Call search_art(word) to get the list of artworks
# 4. API error (search_art returned None)? → back to home.html with an error message
# 5. No results (empty list)? → back to home.html with "No artworks found for '...'"
# 6. Otherwise → show results.html with the artworks and the search word
#    (Missing fields: results.html shows "Untitled" / "Unknown artist" / "Unknown date")