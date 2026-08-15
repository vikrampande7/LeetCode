class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        flag = True
        for x in nums:
            total ^= x
            if x > 0:
                flag = False
        if total > 0:
            return n
        if flag == False:
            return n - 1
        else:
            return 0