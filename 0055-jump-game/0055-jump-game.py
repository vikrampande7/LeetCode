class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # if nums[0] == 0:
        #     return True
        maxReach = 0
        currReach = 0
        for i in range(n):
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= n - 1:
                return True
            if i == currReach:
                if i == maxReach:
                    return False
                else:
                    currReach = maxReach
        return True
        