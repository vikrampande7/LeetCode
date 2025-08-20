class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        maxReach = 0
        currReach = 0
        jump = 0
        for i in range(n):
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= n - 1:
                return jump + 1
            if i == currReach:
                if i == maxReach:
                    return -1
                else:
                    jump += 1
                    currReach = maxReach
        return -1
        