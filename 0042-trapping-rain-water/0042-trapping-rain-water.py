class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        left_max, right_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                ans += left_max - height[l] 
                l += 1
            else:
                right_max = max(right_max, height[r])
                ans += right_max - height[r] 
                r -= 1
        return ans