class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m = [-1] * len(cost)

        def rec(i):
            if i >= len(cost):
                return 0
            if m[i] != -1:
                return m[i]
            m[i] =  cost[i] + min(rec(i+1), rec(i+2))
            return m[i]
            
        return min(rec(0), rec(1))
        