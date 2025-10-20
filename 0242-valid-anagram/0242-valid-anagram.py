class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = {}
        for c in s:
            one[c] = one.get(c, 0) + 1
        
        two = {}
        for c in t:
            two[c] = two.get(c, 0) + 1

        return one == two
        