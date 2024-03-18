class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min = prices[0]
        max = 0
        # Find mid of prices
        for i in range(1, len(prices)):
            if prices[i] <= min:
                min = prices[i]
            else:
                transaction = prices[i] - min
                if max <= transaction:
                    max = transaction
        return max