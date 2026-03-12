class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            rightSum = total_sum - leftSum - num
            if leftSum == rightSum:
                return i
            leftSum += num
        return -1