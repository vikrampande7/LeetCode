class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        while n > 1:
            isSorted = True
            minSum = float("inf")
            t = -1
            for i in range(n-1):
                pairSum = nums[i] + nums[i+1]
                if nums[i] > nums[i+1]:
                    isSorted = False
                if pairSum < minSum:
                    minSum = pairSum
                    t = i
            if isSorted:
                break
            ans += 1
            nums[t] = minSum
            nums.pop(t+1)
        return ans