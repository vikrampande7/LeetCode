class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i, n in enumerate(nums):
            if (target - n) in hm:
                return [i, hm[target - n]]
            hm[n] = i
        return -1
        