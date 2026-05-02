class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for p in range(1, len(prices)):
            if prices[p] > prices[p-1]:
                maxProfit += prices[p] - prices[p-1]
        return maxProfit 