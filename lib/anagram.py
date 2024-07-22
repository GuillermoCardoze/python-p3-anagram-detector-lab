import ipdb


class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, words):
        return [w for w in words if sorted(w) == self.sorted_word]

