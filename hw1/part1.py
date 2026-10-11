# HW1 Part 1: Strings
# Run it:  python3 part1.py
# Your output must match expected/part1.txt exactly.

artwork = {
    "title": "The Bedroom",
    "artist": "Vincent van Gogh",
    "year": 1889
}

print(f"{artwork["title"]} ({artwork["year"]}) by {artwork["artist"]}")
print(f"{(artwork["title"]).upper()} {len(artwork["title"])}")


print("Bed" in artwork["title"])
