class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums) // 2 + 1
        print(m)
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1
        print(h)
        for k, v in h.items():
            if v >= m:
                return k
        