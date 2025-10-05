class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = -1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                res = m
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if res == -1:
            return [-1, -1]
        else:
            return [res-1, res]