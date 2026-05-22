class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        mp = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                mp = max(mp, (prices[r] - prices[l]))
            r += 1
        return mp