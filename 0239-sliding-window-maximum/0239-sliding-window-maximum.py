class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TLE Solution
        # windowMax = []
        # for i in range(0, len(nums)-k+1):
        #     sublst = nums[i:i+k]
        #     maxLst = max(sublst)
        #     windowMax.append(maxLst)
        # return windowMax
        
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output