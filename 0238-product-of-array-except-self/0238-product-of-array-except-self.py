class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        out = [1] * n
        prefix = 1
        for i in range(1, n):
            out[i] = prefix * nums[i-1]
            prefix = out[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            out[i] = postfix * out[i]
            postfix = postfix * nums[i]
        return out
