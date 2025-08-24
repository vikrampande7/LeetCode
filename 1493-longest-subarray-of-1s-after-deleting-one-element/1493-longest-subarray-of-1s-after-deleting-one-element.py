class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1

        def findMax(nums, idx):
            currLen = 0
            maxLen = 0
            for i in range(n):
                if i == idx:
                    continue
                if nums[i] == 1:
                    currLen += 1
                    maxLen = max(maxLen, currLen)
                else:
                    currLen = 0
            return maxLen

        if ones == n:
            return n - 1
        elif ones == 0:
            return 0
        else:
            for i in range(n):
                if nums[i] == 0:
                    res = max(res, findMax(nums, i))
            return res
        