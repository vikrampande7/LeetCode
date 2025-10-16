class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for p in range(1, len(prices)):
            if prices[p] > prices[p-1]:
                maxProfit += prices[p] - prices[p-1]
        return maxProfit
        