class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] > nums[m+1]:
        #         r = m
        #     else:
        #         l = m + 1
        # return l

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return i 
        return len(nums) - 1

