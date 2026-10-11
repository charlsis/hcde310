# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles

# No. 1
count = 0

for title in titles:
    count += 1
    print(f"{count}. {title} ")

# No. 2
print(f"Titles: {len(titles)}")

# No. 3
count = 0
for title in titles:
    if "a" in title.lower():
        count += 1

print(f"Titles with an \"a\": {count}")

# No.4
longest = title[0]

for title in titles:
    if len(title) > len(longest):
        longest = title

print(f"Longest: {longest}")