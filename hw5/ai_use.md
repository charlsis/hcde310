# AI Use

1. What I used it for: understanding the instructions and starter code, writing pytest tests, the AI
   review (step 4), answering my 2 questions, and the fix (step 5). It also helped me
   draft parts of findings.md, which I edited
2. The full chat for step 4:
Review this Flask app for bugs, missing error handling, accessibility and security problems. For each one, point to the line.

app.py:

```python
from flask import Flask, render_template, request

from api import get_artworks

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    artist = (request.values.get("artist") or "").strip()
    if not artist:
        return render_template("home.html", message="No search term entered.")
    try:
        artworks = get_artworks(artist)
    except Exception as e:
        return render_template("home.html", message=f"Something broke the request: {e}")
    return render_template("results.html", artist=artist, artworks=artworks)


if __name__ == "__main__":
    app.run(debug=True)

```


api.py:

```python
import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display,image_id"


def get_artworks(artist):
    params = {"q": artist, "fields": FIELDS, "limit": 10}
    headers = {"User-Agent": "hcde310-artist-search/1.0"}
    response = requests.get(URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json().get("data", [])[:10]

```

Here's my review, grouped by type, with the line for each. Line numbers count from the top of each file (blank lines included).

## Bugs and logic problems

1. **api.py, line 8: `"q": artist` searches everything, not just artists.**
   `q` matches any text (titles, descriptions, artist names), so a search for "Monet" can return works *about* or *near* Monet, not only works *by* him. And because the search is fuzzy, a made-up word still returns weak matches. Nothing checks how good a match is (the API's `_score`) or whether `artist_title` actually matches, so the "No results found" message in `results.html` will almost never appear.

2. **app.py, line 13 (and `home.html`, the `<form method="post">`): the search uses POST.**
   POST is meant for actions that change something. For a search, GET is better: the URL would show `/results?artist=Monet`, so users can bookmark, share, and refresh it. With POST, refreshing asks "resubmit form?" and the URL has no search word.

3. **`results.html`: `artist_title` is requested (api.py line 4) but never shown.**
   The app is an *artist* search, but the results don't say who made each work, so users can't tell which results are actually by the artist they searched.

4. **`results.html`: no default for a missing title.**
   `{{ art.title }}` has no fallback, so an artwork with no title shows an empty heading and gets `alt=""` on its image. The date has a fallback ("Date unknown"), but the title doesn't.

5. **api.py, line 12: `[:10]` is redundant.**
   `limit: 10` (line 8) already asks for 10 results. Not harmful, just extra.

## Error handling

6. **app.py, line 20: `except Exception` is too broad.**
   It catches *every* error, including bugs in your own code (like a typo), and shows them as if the API failed. Catching `requests.RequestException` would only catch network and API errors.

7. **app.py, line 21: shows the raw error `{e}` to the user.**
   Users see technical text like "500 Server Error... for url: https://api.artic.edu/..." This is confusing, and it reveals internal details (the API address and query). A friendly message like "We couldn't reach the Art Institute. Please try again later." is better, with the details printed to the terminal for the developer.

8. **api.py, line 12: `response.json()` can fail** if the API sends back something that isn't JSON (like an HTML error page). That error also lands in the broad `except` and shows raw to the user.

## Accessibility

9. **`results.html`: the image `alt` just repeats the title,** which is already the heading right above it, so screen reader users hear the title twice. Something like `alt="Image of {{ art.title }}"`, or a blank `alt=""` since the heading already names it, would be clearer. And if the title is missing, the alt is empty (see #4).

10. **`home.html`: the message isn't announced.** The error/empty message is a plain `<p>`, so a screen reader may not notice it appeared. Adding `role="alert"` to that `<p>` would make it read aloud.

    *What's good:* the label is properly connected to the input (`for="artist"` / `id="artist"`), the page has a `lang`, and there's a "New search" link.

## Security

11. **app.py, line 26: `app.run(debug=True)`.**
    Debug mode shows an interactive debugger when something crashes, which lets anyone who can open the page run code on the server. Fine on your laptop, dangerous if this were ever put online.

12. **app.py, line 21: leaking error details** (same as #7) is also a small security issue, since it reveals how the backend works.

    *What's good:* Flask's templates escape user input automatically, so typing HTML or a script into the search box won't run on the page. And there are no secret API keys in the code.

## Not sure from the code alone

13. **Images may not load.** The image URL in `results.html` matches the format in `prompt.md`, so the code looks right. If images show as broken boxes, the cause is likely outside this code (for example, the image server not responding to that request). The template has no fallback when an image *fails* to load, only when `image_id` is missing.

---

Send your 2 questions next. After that, compare this list with your 6 checks for `findings.md`.

1. Why does the /results route have methods=["GET", "POST"]?
2. What does response.raise_for_status() do?

**1. Why does `/results` have `methods=["GET", "POST"]`?**

A browser can send form data two ways:
- **GET** puts it in the URL (`/results?artist=Monet`).
- **POST** hides it inside the request instead.

By default, a Flask route only accepts **GET**. This app's form uses `method="post"`, so the route **must** list `"POST"`, or Flask would reject the search with a "405 Method Not Allowed" error. Copilot listed **both** so the route works either way, and it uses `request.values`, which reads the search word from GET **or** POST.

For a search, GET alone would be better, since it lets users bookmark, share, and refresh the results.

**2. What does `response.raise_for_status()` do?**

It checks the API's status code. If it's an **error code** (400s or 500s, like 404 or 500), it **raises an error** (stops and throws) right on that line. If it's **200 (OK)**, it does nothing and the code continues.

It's a shortcut for what you wrote in HW4: `if r.status_code != 200: return None`. The difference is that instead of returning `None`, it throws an error, which jumps to the `except` in `app.py`. That's why your broken-URL test showed "Something broke the request: 500 Server Error..."

---

## Now fill in section 4 of findings.md

Compare the review with your 6 checks. Write these **in your own words**:

- **What it found that I missed:** things the AI listed that aren't in your checks. For example: `q` searches all text, not just artists; the artist name is never shown; no default for a missing title; `except Exception` is too broad; `debug=True` is risky online; the message isn't announced to screen readers.
- **What it got wrong:** anything it said that your testing showed differently. One idea: it **couldn't run the app**, so it was only "not sure" about images, while you **proved** they don't load. If you think nothing was wrong, it's fine to say that honestly.
- **Answers to my two questions:** a short version of the two answers above, in your words.

Tell me when that's written, and we'll do **Step 5: the fix**.

4. What the AI wrote: 3 pytest tests in test_app.py (I adjusted them), the friendly
   error message fix in app.py.
   
5. Reflection: The AI helped me most with things I didn't understand. When the instructions were confusing, like what "boxes and arrows" meant or why I needed pytest tests when I could just test in the browser, it explained them in plain English with examples. It also helped me understand code I hadn't seen before, like raise_for_status(). Having it explained step by step made it less overwhelming. But I learned that the AI review isn't enough on its own like it couldn't tell that the images were broken because it didn't run the app. I only found that by testing it myself first.