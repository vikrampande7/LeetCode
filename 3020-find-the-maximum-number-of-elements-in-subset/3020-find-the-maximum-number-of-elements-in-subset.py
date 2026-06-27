class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        oneCnt = cnt.get(1, 0)
        ans = oneCnt if oneCnt % 2 else oneCnt - 1
        cnt.pop(1, None)
        for num in cnt:
            res = 0
            x = num
            while x in cnt and cnt[x] > 1:
                res += 2
                x *= x
            ans = max(ans, res + (1 if x in cnt else -1))
        return ans