class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s = nums[1:]
        s.sort()
        return nums[0] + s[0] + s[1]