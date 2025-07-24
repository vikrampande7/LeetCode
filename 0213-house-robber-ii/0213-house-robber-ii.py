class Solution:
    def rob(self, nums: List[int]) -> int:

        def house_robber(nums):
            r1, r2 = 0, 0
            for num in nums:
                maxSum = max(num+r1, r2)
                r1 = r2
                r2 = maxSum
            return maxSum

        if len(nums) == 1:
            return nums[0]

        return max(house_robber(nums[1:n]), house_robber(nums[:-1]))
        