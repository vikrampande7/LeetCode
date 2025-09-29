from functools import lru_cache
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @lru_cache(None)
        def solve(i, j):
            if j - i + 1 < 3:
                return 0
            res = float("inf")
            for k in range(i+1, j):
                currWeight = (values[i] * values[k] * values[j]) + solve(i, k) + solve(k, j)
                res = min(res, currWeight)
            return res

        n = len(values)
        return solve(0, n-1)      