import re


def generate_words(message):
    word = re.findall("\w+", message)
    start = 0
    while start < len(word):
        yield word[start]
        start += 1


for w in generate_words("...!!!!мама!!!!   ????мыла....     ????раму"):
    print(w)
