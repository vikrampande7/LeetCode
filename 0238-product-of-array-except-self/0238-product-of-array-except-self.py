class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefixSum = [1] * len(nums)
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            prefixSum[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            prefixSum[i] *= postfix
            postfix *= nums[i]
        return prefixSum
