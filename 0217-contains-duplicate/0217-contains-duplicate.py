class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        u = set()
        for n in nums:
            if n in u:
                return True
            u.add(n)
        return False
        