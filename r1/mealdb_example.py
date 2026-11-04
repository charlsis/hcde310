# mealdb_example.py: find meals by ingredient, then show one full recipe.
import requests

url = "https://www.themealdb.com/api/json/v1/1"    # the "1" is the free test key

# --- Part 1: search by ingredient ---
ingredient = "zzzz"
r = requests.get(f"{url}/filter.php", params={"i": ingredient}, timeout=10)

if r.status_code != 200:
    print("Sorry, the search didn't work:", r.status_code, r.reason)
else:
    meals = r.json()["meals"]

    # No results come back as None or the text "no data found", not an empty list
    if meals is None or meals == "no data found":
        print(f"No meals found with {ingredient}.")
    else:
        print(f"{len(meals)} meals use {ingredient}:")
        for meal in meals[:3]:                       # just the first 3
            print("-", meal["strMeal"])

        # --- Part 2: get the full recipe for the first meal ---
        first_id = meals[0]["idMeal"]
        r2 = requests.get(f"{url}/lookup.php", params={"i": first_id}, timeout=10)
        recipe = r2.json()["meals"][0]

        print()
        print(recipe["strMeal"], "|", recipe.get("strArea"), recipe.get("strCategory"))

        # Ingredients aren't a list: they're separate keys strIngredient1, strIngredient2, ...
        for n in [1, 2, 3, 4, 5]:                    # the first 5 ingredients
            ing = recipe.get(f"strIngredient{n}")
            amount = recipe.get(f"strMeasure{n}")
            if ing:                                   # skip empty ones
                print("  ", amount, ing)