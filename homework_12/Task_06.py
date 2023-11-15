def generate_words(message):
    word = message.split()
    start = 0
    while start < len(word):
        yield word[start]
        start += 1


for w in generate_words("мама мыла раму"):
    print(w)