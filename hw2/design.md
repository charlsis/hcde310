# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
Because each artwork is a separate item and this makes it easier to look through all artworks and get each of their details. A big dictionary is useful to look up artworks by their unique key, but a list of dictionaries is better for storing and processing a collection of artworks, since in a big dictionary it's harder to organize multiple artworks where some might have the same key.


## 2. Which fields are sometimes missing? What should the app show when they are?
The year, medium, artist, and title are sometimes missing. The app should show "unknown" instead of causing error.
