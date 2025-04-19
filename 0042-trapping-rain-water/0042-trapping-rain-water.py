class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        maxLeft = [0] * n
        maxRight = [0] * n

        # Find Maximum Height on Left
        maxLeft[0] = height[0]
        for l in range(1, n):
            maxLeft[l] = max(maxLeft[l-1], height[l])

        # Find Maximum Height on Left
        maxRight[n-1] = height[n-1]
        for r in range(n-2,-1,-1):
            maxRight[r] = min(maxRight[r+1], height[r])

        # out = min(leftheightmax, rightheightmax) - currentheight
        out = 0
        for i in range(n):
            out += min(maxLeft[i], maxRight[i]) - height[i]

        return out