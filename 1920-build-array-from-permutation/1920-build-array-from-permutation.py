class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out = []
        for i, num in enumerate(nums):
            out.append(nums[num])
        return out
        