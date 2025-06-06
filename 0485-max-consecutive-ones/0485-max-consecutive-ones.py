class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, max_1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
                if curr > max_1:
                    max_1 = curr
            else:
                curr = 0
        return max_1
        