class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if all(prices[i] >= prices[i+1] for i in range(len(prices) - 1)):
            return 0

        l = 0 # buy
        r = 1 # sell
        max_diff = 0
        
        while l <= r and r < len(prices):
            diff = prices[r] - prices[l]
            max_diff = max(diff, max_diff)
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r+= 1
        
        return max_diff

        '''max_diff = 0

        for i in range(len(prices) - 1):
            j = i
            while j < len(prices):
                diff = prices[j] - prices[i]
                max_diff = max(diff, max_diff)
                j+=1
        
        return max_diff'''