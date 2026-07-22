class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = 1
        for i in range(0, n):
            t = t * 2 * (2 * i + 1) / (i + 2)
        return int(t)