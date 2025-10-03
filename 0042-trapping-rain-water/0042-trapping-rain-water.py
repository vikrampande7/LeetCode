class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        maxLeft = [0] * n
        maxRight = [0] * n

        # Maximum height to the left of each bar
        maxLeft[0] = height[0]
        for l in range(1, n):
            maxLeft[l] = max(maxLeft[l - 1], height[l])

        # Maximum height to the right of each bar
        maxRight[n - 1] = height[n - 1]
        for r in range(n - 2, -1, -1):
            maxRight[r] = max(maxRight[r + 1], height[r])  

        # Compute total trapped water
        out = 0
        for i in range(n):
            out += min(maxLeft[i], maxRight[i]) - height[i]

        return out
