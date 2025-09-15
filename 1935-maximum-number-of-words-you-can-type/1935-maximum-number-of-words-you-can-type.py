class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        res = len(words)
        for word in words:
            for c in brokenLetters:
                if c in word:
                    res -= 1
                    break
        return res