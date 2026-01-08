class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new = [0] * 2*n
        for i in range(n):
            new[i] = nums[i]
            new[i+n] = nums[i]
        return new
        