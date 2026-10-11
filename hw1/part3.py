# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

# No. 1
i = 0

for year in years:
    if year > cutoff:
        print(titles[i])
    i += 1

# No. 2
print()

i = 0

for year in years:
    if year < cutoff:
        print(f"{titles[i]}: old")
    else:
        print(f"{titles[i]}: modern")
    i += 1

# No.3
print()

old_count = 0
modern_count = 0

for year in years:
    if year < cutoff:
        old_count += 1
    else:
        modern_count += 1

print(f"Old: {old_count}")
print(f"Modern: {modern_count}")




