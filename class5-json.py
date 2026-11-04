# import json
# with open("aic_sample.json") as f:
#     data = json.load(f)

# results = data["data"]
# print(results)

# first = results[0]
# first_title = data["data"][0]["title"]
# print(first_title)

# # total number of resuls
# print(data["pagination"]["total"])

# # 2nd result's title
# print(data["data"][1]["title"])

# # 1st result's artist
# print(data["data"][0]["artist_title"])

# # Image ID
# print(data["data"][0]["image_id"])

# print(data["data"][2]["artist_title"])
# if print(data["data"][0]["artist_title"]) == None:
#     print("unknown Artist")

# art = data["data"][2]
# print("By " + art["artist_title"])
# if art["artist_title"]:
#     print("By" + art["artist_title"])
# else:
#     print("No artist found")

url = "https://api.artic.edu/api/v1/artworks/search"
import requests
r = requests.get(url, params={"q": "cats"})
if r.status_code == 200:
    data = r.json()


