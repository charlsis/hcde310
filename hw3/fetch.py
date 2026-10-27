# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,place_of_origin,dimensions,thumbnail"


# Functions go here (above the code that runs)
# PART 3
def count_by_artist(results):
    counts = {}
    for art in results:
        a = art.get("artist_title") or "Unknown"
        counts[a] = counts.get(a, 0) + 1
    return counts

# PART 4
def save_results(artworks, filename):
    with open(filename, "w") as f:   
        for art in artworks:
            titles = art.get("title") or "Untitled"
            artist = art.get("artist_title") or "Unknown Artist"
            date = art.get("date_display") or "Unknown date"
            f.write(f"{titles} by {artist} on {date}")

# PART 2
term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"
params = {"q": term, "fields": FIELDS}
response = requests.get(url, params=params)


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

        print("Artworks per artist:", count_by_artist(results))
        save_results(results, "ResultStorage.txt")   



# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results



   