class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n+1)
        dp[1] = 1
        k = 0
        for d in range(2, n+1):
            if d - delay > 0:
                k = (k + dp[d-delay]) % mod
            if d - forget > 0:
                k = (k - dp[d-forget]) % mod
            dp[d] = k
        total = sum(dp[n-forget+1: n+1]) % mod
        return total
        