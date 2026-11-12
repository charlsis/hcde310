# HW5 findings

## 1. Drawing: one search for "Monet"
![Drawing of one search for Monet](drawing.jpg)

## 2. Two questions about the code
1. methods=["GET", "POST"]. Why are both methods written in /results
2. what does response.raise_for_status() do?

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
|---|---|---|
| 1 | (pytest) Home page shows the search form with an "Artist name" label | Pass |
| 2 | (pytest) Empty search → "No search term entered" message | Pass |
| 3 | (pytest) Search "Monet" → results page with artworks listed | Pass |
| 4 | (pytest) Made-up word "zzzz" → "No results found" | **Fail**: it showed real artworks (like American Gothic). The API's fuzzy search returns weak matches: "zzzz" scored about 0.000025 vs. about 130 for "monet", but the app shows them anyway. |
| 5 | API error (broken URL) → friendly message | **Fail**: it shows a technical error ("500 Server Error...") and the full API URL. |
| 6 | Each artwork shows its image (from prompt.md) | **Fail**: images show as broken boxes with a "?" and only the alt text. |

## 4. AI review
What it found that I missed: 
- The results page never shows who made each artwork. The app asks the API for
  `artist_title`, but `results.html` doesnt displays it, so users can't tell which
  results are actually by the artist they searched.
- `app.run(debug=True)` (app.py, line 26). Debug mode is fine on my laptop, but if the
  app were put online, the error page would let anyone run code on the server.
What it got wrong:
The AI only read the code and never ran the app, so it said the image code "looks
right" and was only unsure whether images load. When I actually tested it, every image 
showed as a broken box with a "?"
Answers to my two questions, in my own words:
1. Flask routes only accept GET by default. The form sends the
   search with POST, so the route has to list POST or it would give an error. Listing
   both lets it work either way
2. response.raise_for_status() checks the status code. If it's an error like 404 or
   500, it stops and gives an error, which goes to the `except` in app.py. If it's 200,
   nothing happens and the code keeps going. It's like my HW4 `if r.status_code != 200`

## 5. My fix
What was wrong:
What I changed:
How I checked it works:
Commit before: (hash)  Commit after: (hash)

## 6. Can we ship it? (100–150 words)
Yes or no, and why:

One thing my HW4 does better:
One thing the AI's app does better:

AI use goes in `ai_use.md` (the five points on the AI Use Card).
