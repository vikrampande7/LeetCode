class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return abs(nums[1]-nums[0])

        maxDiff = 0
        circDiff = abs(nums[0]-nums[-1])
        maxDiff = max(maxDiff, circDiff)

        for i in range(0, len(nums)-1):
            diff = abs(nums[i+1]-nums[i])
            maxDiff = max(maxDiff, diff)

        return maxDiff
        