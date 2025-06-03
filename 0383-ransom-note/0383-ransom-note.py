class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}

        for c in magazine:
            m[c] = m.get(c, 0) + 1

        for c in ransomNote:
            if c not in m:
                return False
            elif m[c] == 0:
                return False
            m[c] -= 1
        
        return True

        