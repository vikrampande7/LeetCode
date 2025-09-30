class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            newNums = []
            for i in range(n-1):
                ts = (nums[i] + nums[i + 1]) % 10
                newNums.append(ts)
            nums = newNums
            n = len(nums)
        return nums[0] 