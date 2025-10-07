class Solution:
    def climbStairs(self, n: int) -> int:
        ## DP
        # if n == 1:
        #     return 1
        # dp = [0 for _ in range(n+1)]
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        ## Fibonacci
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second