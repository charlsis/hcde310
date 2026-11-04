# def label(year):
#     if year < 1900:
#         return "old"
#     return "modern"

# print(label(1889),label(1942))

titles = ["Nighthawks", "The Bedroom", "Sky above Clouds IV"]
for t in titles:
    if "the" in t.lower():
        print(t)

# Turn into Function
def titles_with(word, titles):
    """ Returns a list of titles with the word in it"""
    titles_with_word = []
    for t in titles:
     if word in t.lower():
        titles_with_word.append(t)
    return titles_with_word

titles_with("the", titles)

myList = ["cats", "dogs", "goats"]
for i in range(len(myList)): # or for i, value in enumerate(myList): for both value and index
    print(f"{i + 1}. {myList[i]}")

