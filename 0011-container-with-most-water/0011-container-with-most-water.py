class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            h = min(height[l], height[r])
            b = r - l
            curr_water = b * h
            max_water = max(curr_water, max_water)
            
            if height[l] < height[r]: ########## You missed this point, move the pointer where wall is shorted
                l += 1
            else:
                r -= 1
        return max_water
        