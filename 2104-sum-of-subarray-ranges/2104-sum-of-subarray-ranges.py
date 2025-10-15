class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for l in range(n):
            largest, smallest = float("-inf"), float("inf")
            for r in range(l, n):
                largest = max(largest, nums[r])
                smallest = min(smallest, nums[r])
                total += largest - smallest
        return total