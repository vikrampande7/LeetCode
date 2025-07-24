class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0
        for n in nums:
            maxSum = max(n+r1, r2)
            r1 = r2
            r2 = maxSum
        return maxSum 
        

        