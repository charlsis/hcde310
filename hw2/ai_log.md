# HW2 Part 6 – AI log (`ai_log.md`)

The tutor walks you through the routine (Try → Predict → Run → Explain → Log) as you chat, so your transcript shows most of it. In `ai_log.md`:

---

## 1. One prediction
*copy one prediction you made in a chat. Were you right? If not, what surprised you?*
['Water Lilies', 'Stacks of Wheat (End of Summer)']
This was my prediction for works_by("Claude Monet", artworks) and I was right.


## 2. What clicked
*pick one thing you were stuck on or didn't know. Without looking at the transcript, explain it in your own words.*
In general, I get a bit confused on where to start writing code from 0. AI helped me think through the overall structure from an empty list, and return in the end. With for loops and using if statements as decider, and counter.


## 3. Too much?
*Did the tutor ever give you too much? What did you do? (one line)*
It explained well, just not straightforward and sometimes becomes confusing bc of that


## 4. Transcripts
*paste every tutor chat you used for HW2 (one is fine if that's all you had)*
```python
"""Ten artworks as dictionaries. Some are missing fields, like real API data.
Don't edit this file. Import from it:  from artworks import artworks
"""

artworks = [
    {"title": "The Bedroom", "artist": "Vincent van Gogh", "year": 1889, "medium": "Oil on canvas"},
    {"title": "Nighthawks", "artist": "Edward Hopper", "year": 1942},
    {"title": "American Gothic", "artist": "Grant Wood", "year": 1930, "medium": "Oil on beaver board"},
    {"title": "A Sunday on La Grande Jatte", "artist": "Georges Seurat", "year": 1884, "medium": "Oil on canvas"},
    {"title": "The Old Guitarist", "artist": "Pablo Picasso", "year": 1903},
    {"title": "Water Lilies", "artist": "Claude Monet", "year": 1906, "medium": "Oil on canvas"},
    {"title": "The Child's Bath", "artist": "Mary Cassatt"},
    {"title": "Sky above Clouds IV", "artist": "Georgia O'Keeffe", "year": 1965},
    {"title": "Stacks of Wheat (End of Summer)", "artist": "Claude Monet", "year": 1890},
    {"title": "Untitled (vase)"},
]

```


```python
# HW2 Part 4 – Your first functions
#
# In `part4.py`, turn code you already wrote into functions:
#
# 1. `works_by(artist, artworks)` → returns a list of titles by that artist, from the list you pass in
#    (an empty list if there are none)
``` How should I start this?

Good question to ask before typing anything. Starting with a plan is a strong habit, and you've already got the data and the goal in front of you.

Your assignment says to "turn code you already wrote into functions," so there's one thing I need to see first: **have you already written code (in an earlier part of this homework or in class) that loops through a list of artworks and collects the titles for one artist?** If so, paste it, even if it's rough or only partly works. If not, tell me that and we'll start from a blank page.

Once I can see where you are, we'll move to Predict.

```python
# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks

artist_counts = {}

for artwork in artworks:
    artist = artwork.get("artist", "Unknown")

    if artist in artist_counts:
        artist_counts[artist] += 1
    else:
        artist_counts[artist] = 1

print(artist_counts)

# Artist with the most work
counts = {}

for artwork in artworks:
    a = artwork.get("artist", "Unknown")
    counts[a] = counts.get(a, 0) + 1

print(counts)

most_artist = ""
most_count = 0

for a in counts:
    if counts[a] > most_count:
        most_artist = a
        most_count = counts[a]

print(f"Most works: {most_artist} ({most_count})")


```
Thanks, that gives me something to work with. Your Part 3 loop (go through each artwork, look at its artist, do something with it) is the same shape you'll need for `works_by`. That's what "turn code you already wrote into functions" is pointing at.

Before any code, let's pin down what the function should do. **If you called `works_by("Claude Monet", artworks)` on your list, what exact value should come back?** Write out what you'd expect to see, brackets and all.

['Water Lilies', 'Stacks of Wheat (End of Summer)']

Yes, that's exactly right: a list with two titles, in the order they appear in your data. You were also careful to return titles, not the whole dictionaries.

Now a related prediction. **What should `works_by("Frida Kahlo", artworks)` return, given that no artwork in the list has that artist?** Check your assignment text for a hint.

[]

Right again: an empty list, `[]`, matching what the assignment says to return when there are no matches.

Now notice something about both of your answers. In each case the function starts with an empty list and fills it with titles as it goes, and if nothing matches, it stays empty.

Here's the next question, about your own Part 3 code. **Which part of your loop decided whether an artwork "counted"? And what would that check need to compare in `works_by`?** Describe it in words first, and don't write any code yet.

I think we start with an empty list, so we assign, let, let's say the name is count equals to an empty list, empty bracket, and then we decide the loop is counted by using an if statement. And we return it in the end.

You've got the overall shape: start with an empty list, loop through the artworks, use an `if` to decide which ones belong, and return the list at the end.

**What you got right:** the empty list at the start, the `if` as the decider, and `return` coming after the loop finishes.

**What's still missing:** you haven't said what the `if` compares. You also didn't mention the loop itself, which is what visits each artwork one at a time.

One small note: `count` usually suggests a number, like in Part 3. Since this list holds titles, you might pick a name that says so.

Now the missing piece. **In your Part 3 loop, each `artwork` is a dictionary. For `works_by`, which two things should the `if` compare to decide whether an artwork belongs in the list?** Tell me in words, one from the artwork and one from the function's inputs.

Okay, then just like put a for loop and count. Instead of count, then we do titles equals empty bracket to represent a list. The if statement, add the, the for loop, and then the if statement, and return.

You've renamed `count` to `titles`, and your structure is solid: start with an empty list, loop, `if`, then `return` after the loop.

**What you got right:** the order of the pieces, and that the list gets filled inside the `if`.

**What's still missing:** the `if` itself. Twice now I've asked what it compares, and your answer has described the outline again. That's the one part you haven't put into words yet, so let's slow down on it.

Here's a tiny example with different data. Say I'm collecting songs of one genre:

```python
if song["genre"] == wanted_genre:
```

**In this line, what is being compared to what, and where does each side come from?** (Is one side from the thing the loop is looking at, and the other from something the function was given?)

Once you can say that, you'll be ready to map it onto artworks and write your first attempt.

the artist.

You're close, and "the artist" is the right topic. But there are two sides to that comparison, so let's pull them apart.

In my example, `song["genre"]` comes from the song the loop is currently looking at. `wanted_genre` comes from outside the loop: it's something the function was handed.

**For `works_by`, the loop looks at one `artwork` at a time. Where does the artist on the left side of your comparison come from, and what's the name of the *other* artist, the one the function was handed?** Look at the first line of the assignment for that second name.

if artwork.get("artist") == artist:

That line is a correct comparison, and it's your own work. The left side, `artwork.get("artist")`, comes from the artwork the loop is looking at. The right side, `artist`, is the name the function was handed. You also reused the `.get` habit from Part 3.

Now the Predict step. Your data has `{"title": "Untitled (vase)"}`, which has no `"artist"` key at all.

**When the loop reaches that artwork, what do you think `artwork.get("artist")` gives back, and what does the `if` do with it when you call `works_by("Claude Monet", artworks)`?** Will it crash, match, or skip? Commit to a guess before you run anything.

```python
def works_by(artist, artworks):
    """Takes an artist and a list of artworks, and returns a list of their titles."""
    titles = []
    for artwork in artworks:
        if artwork.get("artist") == artist:
    return titles
```
You've put the whole outline into real code: a clear docstring, `titles` as the list name, the loop, your `if` comparison, and `return` placed after the loop. The structure is right.

I'll park my question about the "Untitled (vase)" artwork for a moment, because I want to run your function through Predict first.

**If you ran this file exactly as it is now, what do you think Python will do?** Will it print something, give an error, or quietly do nothing? Look closely at the line right after the `if` before you answer. Then run it and tell me what happened.
