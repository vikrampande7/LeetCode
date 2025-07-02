class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        curr = ""
        for letter in word:
            if letter == curr:
                res += 1
            else:
                curr = letter
        return res