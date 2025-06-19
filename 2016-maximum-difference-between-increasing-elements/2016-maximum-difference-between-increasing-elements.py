class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = 0
        for j in range(len(nums)-1, -1, -1):
            for i in range(j, -1, -1):
                if i < j and nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    maxDiff = max(maxDiff, diff)

        return maxDiff if maxDiff != 0 else -1