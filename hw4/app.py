# app.py: routes for my art search app.
# Who it's for: art students looking up artworks from the Art Institute of Chicago.

# Import Flask tools (Flask, render_template, request)
from flask import Flask, render_template, request
# Import my search_art function from api.py
from api import search_art

# Create the app
app = Flask(__name__)

# ---------- / (home) ----------
# Show home.html, which has the search form.
@app.route("/")
def home():
   return render_template("home.html")
# (If /results sends the user back with a message, home.html shows it.)


# ---------- /results ----------
@app.route("/results")
def results():
    # 1. Read the search word the user typed in the form
    word = request.args.get("search", "")

    # 2. Empty input? → back to home.html with "Please type a search word."
    if word.strip() == "":
            return render_template("home.html", message="Please type a search word.")

    # 3. Call search_art(word) to get the list of artworks
    artworks = search_art(word)

    # 4. API error (search_art returned None)? → back to home.html with an error message
    if artworks is None:
        return render_template("home.html", message="We couldn't reach the Art Institute right now. Please try again in a few minutes.")

    # 5. No results (empty list)? → back to home.html with "No artworks found for '...'"
    if len(artworks) == 0:
            return render_template("home.html", message=f"No artworks found for '{word}'. Try another word.")

    # 6. Otherwise → show results.html with the artworks and the search word
    return render_template("results.html", artworks=artworks, word=word)

    #    (Missing fields: results.html shows "Untitled" / "Unknown artist" / "Unknown date")