class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            h = max(l, r)
            b = r - l
            curr_water = b * h
            max_water = max(curr_water, max_water)
            l += 1
            r -= 1
        return max_water
        