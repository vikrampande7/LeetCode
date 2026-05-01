class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        count = 0
        for start in nums:
            if start-1 not in numsSet:
                end = start + 1
                while end in numsSet:
                    end += 1
                count = max(count, end-start)
        return count
        