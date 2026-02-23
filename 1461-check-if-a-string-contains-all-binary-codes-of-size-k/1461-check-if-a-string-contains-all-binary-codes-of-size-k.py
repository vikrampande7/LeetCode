class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()
        for i in range(k, len(s)+1):
            ss = s[i-k:i]
            if ss not in got:
                got.add(ss)
                need -= 1
                if need == 0:
                    return True
        return False
        