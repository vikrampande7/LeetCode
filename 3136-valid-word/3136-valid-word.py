class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        consonants = [
            "B", "b", "C", "c", "D", "d", "F", "f", "G", "g",
            "H", "h", "J", "j", "K", "k", "L", "l", "M", "m",
            "N", "n", "P", "p", "Q", "q", "R", "r", "S", "s",
            "T", "t", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"
        ]

        if len(word) < 3:
            return False

        for w in word:
            if w not in vowels or w not in consonants:
                return False

        return True if word.isalpha() and word.isalnum() else False

        