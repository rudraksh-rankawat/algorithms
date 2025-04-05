class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0 

        buy, sell = 0, 1
        maxProfit = 0
        while sell < len(prices):
            
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
                sell += 1

        return maxProfit
        