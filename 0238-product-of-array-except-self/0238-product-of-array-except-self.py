class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # easy way: product of all elements in array and divide by each element
        # edge case - division by zero
        # Best approach -> prefix, postfix -> Neetcode
        res = [1] * len(nums)
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res