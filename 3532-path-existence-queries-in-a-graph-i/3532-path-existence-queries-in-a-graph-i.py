class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        tags = [0] * n
        for i in range(1, n):
            tags[i] = tags[i-1] + (1 if nums[i] - nums[i-1] > maxDiff else 0)
        return [tags[x] == tags[y] for x, y in queries]
        