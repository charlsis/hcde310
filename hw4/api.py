# api.py: gets artworks from the Art Institute of Chicago API.
import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display"


def search_art(term):
    """Takes a search word and returns a list of artworks, or None if the API fails."""
    try:
        r = requests.get(URL,
                         params={"q": term, "fields": FIELDS, "limit": 10},
                         headers={"User-Agent": "HCDE310 art search app"},
                         timeout=10)
    # Runs if the API never answers (no wifi, wrong address)
    except requests.RequestException:
        print("API error: no answer")
        return None

    # The API answered with an error (like 404 or 500), so return None
    if r.status_code != 200:
        print("API error:", r.status_code, r.reason)
        return None

    return r.json()["data"]