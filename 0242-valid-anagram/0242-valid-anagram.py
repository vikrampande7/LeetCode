class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        so, to = {}, {}
        for c in s:
            so[c] = so.get(c, 0) + 1
        for c in t:
            to[c] = to.get(c, 0) + 1
        return so == to