class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            if (target - num) in hashmap:
                return [i, hashmap[target-num]]
            hashmap[num] = i 