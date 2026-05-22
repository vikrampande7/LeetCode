class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        print(freq)
        return heapq.nlargest(k, freq, key=freq.get)