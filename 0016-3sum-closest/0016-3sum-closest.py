class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float("inf")
        for i in range(len(nums)):
            low, high = i+1, len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if abs(target - s) < abs(diff):
                    diff = target - s
                if s < target:
                    low += 1
                else:
                    high -= 1
                if diff == 0:
                    break
        return target - diff