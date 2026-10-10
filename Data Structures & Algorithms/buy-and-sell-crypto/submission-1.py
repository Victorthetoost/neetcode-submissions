class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #have to buy at a low price and sell at a high
        maxProfit = 0
        for x in range(0, len(prices)):
            #buy
            for y in range(x + 1, len(prices)):
                #sell
                maxProfit = max(prices[y] - prices[x], maxProfit)
        return maxProfit