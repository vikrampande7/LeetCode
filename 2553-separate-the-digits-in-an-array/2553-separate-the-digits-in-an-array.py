class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for num in nums:
            for digit in str(num):
                out.append(int(digit))
        return out
        