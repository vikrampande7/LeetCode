class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res = []
        nums.sort()

        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return False
            elif nums[i] == nums[i+1]:
                res.append([i, i+1])

        if len(res) == len(nums) / 2:
            return True
        