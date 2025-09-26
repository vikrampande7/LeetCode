class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(0, n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    if (nums[i] + nums[j] > nums[k]) and (nums[i] + nums[k] > nums[j]) and (nums[k] + nums[j] > nums[i]):
                        res += 1
        return res 