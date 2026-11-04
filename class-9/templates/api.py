# api.py

import requests
def find_books(author):
   r = requests.get("https://openlibrary.org/search.json",
                    params={"author": author}, timeout=10)
   return r.json()["docs"][:10]