years = [1889, 1942, 1930, 1973]
for y in years:
    if y < 1900:
        print("old")
    elif y < 1950:
        print("mid-century")
    else:
        print("recent")

if y >= 1900 and y < 1950:
    print("first half of the 20th century")


# results = [a,b,c]
# results = []
#    if results:
#       print()


# phone = {"Ana":"555-1234:", "Sam": "666-6789"}
# print(phone["Ana"])

art = {"title":"The Bedroom",
       "artist":"Vincent van Gogh",
       "year": 1889}
print(art["title"])
    