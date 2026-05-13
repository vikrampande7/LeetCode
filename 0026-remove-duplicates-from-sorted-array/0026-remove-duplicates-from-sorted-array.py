class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        ins = 1
        for i in range(1, size):
            if nums[i-1] != nums[i]:
                nums[ins] = nums[i]
                ins += 1
        return ins
        