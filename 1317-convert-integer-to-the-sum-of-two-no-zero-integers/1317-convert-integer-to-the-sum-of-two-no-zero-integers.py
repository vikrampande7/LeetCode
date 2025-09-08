class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res = []
        for a in range(1, n):
            b = n - a
            if '0' in str(a) or '0' in str(b):
                continue
            else:
                res.append(a)
                res.append(b)
                break
        return res
        