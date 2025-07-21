class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        prev = s[0]
        count = 0
        for c in s:
            if c == prev:
                count += 1
            else:
                prev = c
                count = 1
            if count < 3:
                res += c
        return res
        