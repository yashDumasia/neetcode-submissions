class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(0,len(prices)):
            for j in range(0,len(prices)):
                profit = prices[j] - prices[i]
                if profit > max and j > i:
                    max = profit
        return max