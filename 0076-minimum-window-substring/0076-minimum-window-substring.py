class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t == "":
        #     return ""

        tm = {}
        sm = {}

        res = [-1, -1]
        minLen = float("inf")

        l = 0

        for c in t:
            tm[c] = tm.get(c, 0) + 1
        
        countReq = len(tm)
        countHave = 0

        for r in range(len(s)):
            c = s[r]
            sm[c] = sm.get(c, 0) + 1

            if c in tm and sm[c] == tm[c]:
                countHave += 1

            while countHave == countReq:
                if (r-l+1) < minLen:
                    res = [l, r]
                    minLen = r-l+1
                
                sm[s[l]] -= 1
                if s[l] in tm and sm[s[l]] < tm[s[l]]:
                    countHave -= 1
                l += 1
        l, r = res
        return s[l:r+1] if minLen != float("inf") else ""



        