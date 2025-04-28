class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l = 0
        m = 1
        r = 2
        count = 0

        while r <= len(nums) - 1:
            if nums[l] + nums[r] == nums[m] / 2:
                count+=1
            l += 1
            m += 1
            r += 1

        return count