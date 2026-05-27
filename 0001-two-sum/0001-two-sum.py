class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for idx, num in enumerate(nums):
            if (target - num) in hm:
                return [idx, hm[target - num]]
            hm[num] = idx