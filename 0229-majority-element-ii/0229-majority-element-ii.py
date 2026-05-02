class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        freqMap = {}
        out = []
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        for k, v in freqMap.items():
            if v > n/3:
                out.append(k)
        return out