class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []

        def recursion(nums, i, tmp):
            if i >= len(nums):
                res.append(tmp[:])
                return 

            tmp.append(nums[i])
            recursion(nums, i+1, tmp)
            tmp.pop()
            recursion(nums, i+1, tmp)

        return res
        