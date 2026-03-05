class Solution:
    def minOperations(self, s: str) -> int:
        s0 = s1 = 0
        for i in range(len(s)):
            if i %  2 == 0:
                if s[i] == "0":
                    s1 += 1
                else:
                    s0 += 1
            else:
                if s[i] == "1":
                    s1 += 1
                else:
                    s0 += 1
        return min(s0, s1)