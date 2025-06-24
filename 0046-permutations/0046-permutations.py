class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recursion(nums, i):
            if i == len(nums):
                res.append(nums[:])
                return
            for c in range(i, len(nums)):
                nums[i], nums[c] = nums[c], nums[i]
                recursion(nums, i+1)
                nums[i], nums[c] = nums[c], nums[i]

        recursion(nums, 0)
        return res