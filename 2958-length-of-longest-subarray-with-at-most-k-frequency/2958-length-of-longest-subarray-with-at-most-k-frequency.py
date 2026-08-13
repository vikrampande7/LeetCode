class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, st = 0, -1
        freq = Counter()
        for end in range(len(nums)):
            freq[nums[end]] += 1
            while freq[nums[end]] > k:
                st += 1
                freq[nums[st]] -= 1
            res = max(res, end - st)
        return res