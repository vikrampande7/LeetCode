class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ## O(n^2)
        # water = 0
        # for i in range(1, len(height)-1):
        #     l = i - 1
        #     r = i + 1
        #     lm, rm = 0, 0
        #     while l >= 0:
        #         lm = max(lm, height[l])
        #         l -= 1
        #     while r < len(height):
        #         rm = max(rm, height[r])
        #         r += 1
        #     water += max(0, min(lm, rm) - height[i])
        # return water

        # Extra Memory
        # n = len(height)
        # left = [0] * n
        # right = [0] * n
        # right_max = 0
        # left_max = 0
        # for i in range(n):
        #     if height[i] >= right_max:
        #         right_max = max(right_max, height[i])
        #     left[i] = right_max
        # for i in range(n-1, -1, -1):
        #     if left_max <= height[i]:
        #         left_max = max(left_max, height[i])
        #     right[i] = left_max
        # water = 0
        # for i in range(n):
        #     water += max(0, min(left[i], right[i]) - height[i])
        # return water

        n = len(height)
        l = 0
        r = n - 1
        left_max, right_max = 0, 0
        water = 0
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                r -= 1
        return water

