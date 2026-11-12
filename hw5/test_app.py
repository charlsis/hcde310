# HW5 test_app.py: one example test. Add your own below it (step 5).
# Run from this folder:  python3 -m pytest
from app import app


def test_home_shows_search_form():
    client = app.test_client()        # a pretend browser, no server needed
    page = client.get("/")            # like typing "/" in the address bar
    assert page.status_code == 200    # the page loaded
    assert b"Artist name" in page.data  # the form's label is on the page

def test_empty_search_shows_message():
    client = app.test_client()
    page = client.post("/results", data={"artist": ""})       # submit the form with nothing typed
    assert b"No search term entered" in page.data             # the message is on the page

def test_search_shows_results():
    client = app.test_client()
    page = client.post("/results", data={"artist": "Monet"})   # submit the form with a search term
    assert b"Monet" in page.data                               # the search term is on the page

def test_made_up_word_shows_no_results():
    client = app.test_client()
    page = client.post("/results", data={"artist": "zzzz"})  # a word that shouldn't match
    assert b"No results found" in page.data
