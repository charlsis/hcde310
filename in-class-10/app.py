# app.py: the routes for the books app.
# SKELETON: the whole path works (form → /results → results page) with fake data.
# Next: replace one piece at a time, and commit each time something works.
from flask import Flask, render_template, request   # request (Flask), not requests!
from api import get_books

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    # 1. Read the search term from the form
    author = request.args.get("author_search", "")

    # 2. Empty input? → home page + message (check BEFORE calling the API)
    if author.strip() == "":
        return render_template("home.html", message="Please type an author's name to search.")

    # 3. Call the API (fake data for now)
    books = get_books(author)

    # 4. API error? (get_books returned None) → home page + message
    if books is None:
        return render_template("home.html", message="We couldn't reach the book database right now. Please try again in a few minutes.")

    # Missing fields: keep only books that have a title
    good_books = []
    for book in books:
        if book.get("title"):
            good_books.append(book)
    books = good_books

    # 5. No results, or nothing useful to show? → home page + message
    if len(books) == 0:
        return render_template("home.html", message=f"No books found for \"{author}\". Check the spelling or try another author.")

    # 6. Otherwise → results page
    return render_template("results.html", books=books, author=author)
