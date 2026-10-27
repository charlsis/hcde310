# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
def save_results(artworks, filename):
    # txt will be here
    return(results)


## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*
I did this with a tutor from the Mary Gates Hall Tutoring Center, these are some of the AI help, me and my tutor asked. 

Me: 
Part 3 – Count by artist
AI Use: Stage 2 (Tutor)
Bring your `count_by_artist` function from HW2 into `fetch.py`, and print the counts after the results. - The API's field names aren't the same as HW2's. What does the function need to look up now? - Where does the call go? Check: the counts show up when you search, and nothing breaks when there are no results or an error. `check.py` tests this too.
Part 4 – Save the results
AI Use: Stage 3 (Little helper)
Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and commit the `.txt` file it made: that's your proof the live call works.
You may have the AI write this function (about 10 lines) using the [Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt) (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` as you go:

1. Try: paste your own attempt or plan for the function, even if it doesn't work
2. Chat (AI only): paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."
3. Predict, then compare: before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)
4. What surprised me: one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."
5. Change one thing yourself: once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.


thisis the full instructions and im here now

```python
term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"
params = {"q": term, "fields": FIELDS}
response = requests.get(url, params=params)

# TODO step 3: check response.status_code before you use the data
if response.status_code != 200:
    print(f"sorry the search didn't work: {response.status_code} {response.reason}")
else:
    data = response.json()
    results = data["data"]
    if len(results) == 0:
        print(f"No artworks found for '{term}'. Try another word.")
    else:
        for art in results:
            titles = art.get("title") or "Untitled"
            artist = art.get("artist_title") or "Unknown Artist"
            display = art.get("artist_display") or "Unknown Display"
            date = art.get("date_display") or "Unknown date"
            place = art.get("place_of_origin") or "Unknown place"
            size = art.get("dimensions") or "Unknown size"
            thumb = art.get("thumbnail") or {}
            description = thumb.get("alt_text") or "No description"
            print(f"{titles} ({date}) by {artist}")
            print(f"  Artist info: {display}")
            print(f"  From: {place}")
            print(f"  Size: {size}")
            print(f"  Image: {description}")
            print()


# PART 3
def count_by_artist(results):
    counts = {}
    for art in results:
        a = art.get("artist_title") or "Unknown"
        counts[a] = counts.get(a, 0) + 1
    return counts


# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results

def save_results(artworks, filename):
    
    return(results)
```


```python
term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"
params = {"q": term, "fields": FIELDS}
response = requests.get(url, params=params)

# TODO step 3: check response.status_code before you use the data
if response.status_code != 200:
    print(f"sorry the search didn't work: {response.status_code} {response.reason}")
else:
    data = response.json()
    results = data["data"]
    if len(results) == 0:
        print(f"No artworks found for '{term}'. Try another word.")
    else:
        for art in results:
            titles = art.get("title") or "Untitled"
            artist = art.get("artist_title") or "Unknown Artist"
            display = art.get("artist_display") or "Unknown Display"
            date = art.get("date_display") or "Unknown date"
            place = art.get("place_of_origin") or "Unknown place"
            size = art.get("dimensions") or "Unknown size"
            thumb = art.get("thumbnail") or {}
            description = thumb.get("alt_text") or "No description"
            print(f"{titles} ({date}) by {artist}")
            print(f"  Artist info: {display}")
            print(f"  From: {place}")
            print(f"  Size: {size}")
            print(f"  Image: {description}")
            print()


# PART 3
def count_by_artist(results):
    counts = {}
    for art in results:
        a = art.get("artist_title") or "Unknown"
        counts[a] = counts.get(a, 0) + 1
    return counts


# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results

def save_results(artworks, filename):
    
    return(results)
```

im in part 4 in the txt, is there any examples from prev class

Your Class 6 and 7 notes don't have a file-writing example, so here's the one new idea you need.

**Writing a text file in Python**

```python
with open("example.txt", "w") as f:   # open (or create) the file for writing ("w")
    f.write("first line\n")           # \n = start a new line
    f.write("second line\n")
```

`with` closes the file for you when the indented block ends. Every `f.write` adds text, and `\n` ends each line.

**Your `save_results`,

- Open `filename` for writing.
- Loop over `artworks`.
- For each one, get the title, artist, and date with `or` defaults, like your print loop.
- Write one line with those three, ending in `\n`.
- It doesn't need to `return` anything. Its job is to make the file, so remove `return(results)`.

**Two fixes to Part 3**

1. **Move both `def`s to the top**, under `# Functions go here`. Python has to read a function before the code below can call it.
2. **Call the functions after the `for` loop, inside the inner `else`.** That way they only run when there are results, so nothing breaks on errors or empty searches:

```python
        for art in results:
            ...  # your printing
        print(count_by_artist(results))
        save_results(results, "results.txt")
```

Make sure `print(count_by_artist(...))` lines up with `for`, not inside it, or it'll print the counts five times.

Me: do we still need an f string to print

Not always. An f-string is only for putting variables inside text.

- **Printing the counts:** no f-string needed. `print(count_by_artist(results))` prints the whole dictionary as it is.
- **`f.write` in `save_results`:** an f-string is the easiest way, because you're combining three variables into one line:
  ```python
  f.write(f"{title} | {artist} | {date}\n")
  ```
  Without one, you'd have to join the pieces with `+`, which is messier:
  ```python
  f.write(title + " | " + artist + " | " + date + "\n")
  ```

Both work. The f-string is just shorter. The `|` separator is up to you.

Me:
```python
def save_results(artworks, filename):
    with open("ResultStorage.txt", "w") as f:   
        for art in results:
            titles = art.get("title") or "Untitled"
            artist = art.get("artist_title") or "Unknown Artist"
            date = art.get("date_display") or "Unknown date"
            f.write(f"{titles} by {artist} on {date}\n")         
    return(results)



✗ save_results writes a .txt file when you search
   no .txt file appeared after searching for 'cat'
```
Good attempt. The structure is right. There are three fixes in the function and one outside it.

1. **Use the parameter names.** The function receives `artworks` and `filename`, so use those instead of `results` and a hardcoded name:
   - `open(filename, "w")` instead of `open("ResultStorage.txt", "w")`
   - `for art in artworks:` instead of `for art in results:`
   
   It "works" now only because `results` happens to exist outside the function. check.py calls it with its own data and file name.
2. **Remove `return(results)`.** The function's job is writing the file, so it doesn't need to return anything.
3. **Call it.** "No .txt file appeared" most likely means `save_results` never runs. Add this after your `for` loop, lined up with `for`:
   ```python
           save_results(results, "ResultStorage.txt")
   ```
   This is where you choose the file name, not inside the function.

Me:
```python
def save_results(artworks, filename):
    with open(filename, "w") as f:   
        for art in artworks:
            titles = art.get("title") or "Untitled"
            artist = art.get("artist_title") or "Unknown Artist"
            date = art.get("date_display") or "Unknown date"
            f.write(f"{titles} by {artist} on {date}\n")
        
        save_results(artworks, "ResultStorage.txt")   

   

✗ save_results writes a .txt file when you search
   no .txt file appeared after searching for 'cat'

Not there yet. Fix the first ✗ and run again.
```
The call is inside the function itself, so `save_results` would call itself forever, and your main code still never calls it.

**1. Delete that last line from the function.** The function should end at `f.write(...)`:

```python
def save_results(artworks, filename):
    with open(filename, "w") as f:
        for art in artworks:
            titles = art.get("title") or "Untitled"
            artist = art.get("artist_title") or "Unknown Artist"
            date = art.get("date_display") or "Unknown date"
            f.write(f"{titles} by {artist} on {date}\n")
```

**2. Put the call down in your main code**, after your printing loop, lined up with `for`:

```python
    else:
        for art in results:
            ...                     # your printing lines
        print(count_by_artist(results))
        save_results(results, "ResultStorage.txt")   # ← here
```

In the main code, the list is called `results`, so that's what you pass in. Inside the function, it gets called `artworks`.



## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*
My prediction:
Lion (One of a Pair, South Pedestal) by Edward Kemeys on 1893
Nude with Cats by Pablo Picasso on 1901
Baroque Pearl Mounted as a Cat Holding a Mouse by Unknown Artist on 17th century
Cat Making Up by Inagaki Tomoo on 1962
Homesickness by René Magritte on c. 1948
Actual:
```
Lion (One of a Pair, South Pedestal) by Edward Kemeys on 1893Nude with Cats by Pablo Picasso on 1901Baroque Pearl Mounted as a Cat Holding a Mouse by Unknown Artist on 17th centuryCat Making Up by Inagaki Tomoo on 1962Homesickness by René Magritte on c. 1948
```


## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
I thought art.get("artist_title", "Unknown") would handle the null artist, but it returned None because the key exists with a null value. Using or "Unknown" fixed it

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*
```
def save_results(artworks, filename):
    with open(filename, "w") as f:   
        for art in artworks:
            titles = art.get("title") or "Untitled"
            artist = art.get("artist_title") or "Unknown Artist"
            date = art.get("date_display") or "Unknown date"
            f.write(f"on {date}, {artist} created {titles}\n")
```
I changed the line format so date comes first so I can sort out the artworks based on time.