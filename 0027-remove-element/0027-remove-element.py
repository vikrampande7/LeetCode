class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
#         Write Pointer (k): Tracks where the next "valid" element should be placed.
# Scan Pointer (i): Iterates through the entire array.
# Algorithm: As you scan, if nums[i] is not equal to val, copy nums[i] to nums[k] and increment k.
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

        