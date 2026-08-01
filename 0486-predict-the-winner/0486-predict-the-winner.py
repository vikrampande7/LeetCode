class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        def helper(l, r):
            if l == r:
                return nums[l]
            scoreLeft = nums[l] - helper(l+1, r)
            scoreRight = nums[r] - helper(l, r-1)
            return max(scoreLeft, scoreRight)
        return helper(0, n-1) >= 0