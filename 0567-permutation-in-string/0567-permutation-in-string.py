class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n == m:
            if s1==s2:
                return True
        elif n > m:
            return False

        s1 = sorted(s1)

        for i in range(0, m-1):
            sbstr = s2[i:i+n]
            if sorted(sbstr) == s1:
                return True
        
        return False
        