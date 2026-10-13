# Class 4: Five broken snippets

Your name: Charlene Siswanto
Collaborator: Solo

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
exhibit = {"title": "Water Lilies", "room": 243, "year": 1906}
print("Find it in room " + exhibit["Room"])

- Which line breaks? 2nd line
- What error will Python show? (the kind and the message) NameError because the Key name uses uppercase R
- What's the fix? print("Find it in room " + exhibit["room"])

## Snippet 2
exhibit = {"title": "Water Lilies", "room": 243, "year": 1906}
print("Find it in room " + exhibit["room"])

- Which line breaks? 2nd line
- What error will Python show? (the kind and the message) TypeError because it combines a string and integer key
- What's the fix? I would use an f string print(f"Find it in the room {exhibit["room]}")

## Snippet 3
exhibits = ["Water Lilies", "Nighthawks", "The Bedroom"]
for i in range(len(exhibits) + 1):
    print(i + 1, exhibits[i])

- Which line breaks? line 3
- What error will Python show? (the kind and the message) TypeError, because the index is a  number and string at the same time
- What's the fix? print((len(exhibit[i])+1), exhibit[i])

## Snippet 4
def count_visits(visits, room):
    """Return how many visits went to one room."""
    total = 0
    for v in visits:
        if v == room:
            total = total + 1
    return total

visits = [243, 101, 243, 262, 243]
print(count_visits(visit, 243))


- Which line breaks? 5th line
- What error will Python show? (the kind and the message) IndexError as its checking if v is "room" not the index room number
- What's the fix? if v == 243:

## Snippet 5
def longest_title(titles):
    """Return the longest title in a list of titles."""
    longest = ""
    for t in titles:
        if len(t) > len(longest):
            longest = t
    print(longest)

title = longest_title(["Nighthawks", "The Bedroom", "Water Lilies"])
print(title.upper())

- Which line breaks? 3rd line
- What error will Python show? (the kind and the message) Name error, longest is not assigned correctly
- What's the fix? longest = title[t]

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke? line 2
- What error did Python show? KeyError
- What's the fix? use f string > print(f"Find it in room {exhibit["room"]}")

## Snippet 2
- Which line broke? line 2
- What error did Python show? TypeError
- What's the fix? turn the integer into string > print("Find it in room " + str(exhibit["room"]))

## Snippet 3
- Which line broke? line 2
- What error did Python show? IndexError
- What's the fix? Change the range to index 0,1,2 > for i in range(len(exhibits)):

## Snippet 4
- Which line broke? line 10
- What error did Python show? NameError
- What's the fix? change visit to visits > print(count_visits(visits, 243))

## Snippet 5
- Which line broke? Line 7
- What error did Python show? AttributeError
- What's the fix? function is supposed to be return, not print > return(longest)


When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #: 5
- Our guess before asking: changing line 3 to longest = title[t]
- Chat:
```python
def longest_title(titles):
    """Return the longest title in a list of titles."""
    longest = ""
    for t in titles:
        if len(t) > len(longest):
            longest = t
    print(longest)

title = longest_title(["Nighthawks", "The Bedroom", "Water Lilies"])
print(title.upper())
```

Is the error in line 3 

```markdown
longest = title[t]
```
AI Respond:
I can't say yes or no yet, because the code you pasted doesn't match the line you quoted. Line 3 in your paste is `longest = ""`, and nothing in it contains `title[t]`. Either you've changed the code since you ran it, or the version you ran differs from the one you pasted.

Let's start from what Python actually told you. **Can you paste the full error message exactly as it appeared, including the line number it points to?**

Once I have it, I'll ask which line you think it means before I say anything about it.

My Chat:
File "/Users/charlene/hcde310/in-class-4/exercise.py", line 41, in <module>
    print(title.upper())
          ^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'upper'
charlene@Charlenes-MacBook-Air in-class-4 %

AI Respond:
Thanks, that's exactly what I needed.

**What kind of error this is:** An `AttributeError` means your code asked a value for something it doesn't have, like asking a toaster to play music. `'NoneType'` is the type of Python's "nothing" value, `None`. So the message says that something is `None`, and your code tried to use `.upper` on it, which `None` doesn't have.

This error usually means a variable holds `None` when you expected it to hold something useful like a string. The tricky part is that the error shows up where the value is *used*, and the cause often sits somewhere earlier.

**Which line of your code do you think this error points to?** Check the traceback and tell me the line number and what's on it.

- Did it give you too much? What did you do?
Its explanation I think are a little confusing and long, I ended up realizing myself that the code chunk doesn't have a return function
