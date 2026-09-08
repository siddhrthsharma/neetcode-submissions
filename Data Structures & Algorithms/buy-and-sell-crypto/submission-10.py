class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1

        if all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1)):
            return 0

        while l <= r and r < len(prices):
            current_profit = prices[r] - prices[l]
            if current_profit < 0:
                l = r
                r = l + 1
            else:
                profit = max(current_profit, profit)
                r += 1
        
        return profit