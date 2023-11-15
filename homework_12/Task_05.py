import re


class WordIterable:
    def __init__(self, text):
        self.text = re.findall("\w+",text)
        print(self.text)
        self.word = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.word += 1
        if self.word > len(self.text)-1:
            raise StopIteration()
        return self.text[self.word]

for w in WordIterable("!/.мама. !мыла? .раму."):
    print(w)
