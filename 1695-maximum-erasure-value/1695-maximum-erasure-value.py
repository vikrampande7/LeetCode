class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        maxSum = 0
        winSum = 0
        seen = set()

        while r < n:
            if nums[r] in seen:
                seen.remove(nums[l])
                winSum -= nums[l]
                l += 1
            else:
                winSum += nums[r]
                seen.add(nums[r])
                r += 1
                maxSum = max(maxSum, winSum)
        
        return maxSum
        