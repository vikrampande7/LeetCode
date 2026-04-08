class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return nums + nums
        out = []
        for _ in range(2):
            for n in nums:
                out.append(n)
        return out