class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            a = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, a)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return maxArea