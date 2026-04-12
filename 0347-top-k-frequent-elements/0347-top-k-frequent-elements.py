class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        return heapq.nlargest(k, hm.keys(), key=hm.get)