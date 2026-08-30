class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        keep_i = 0
        keep_j = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if (prices[j] - prices[i] > prices[keep_j] - prices[keep_i]):
                    keep_i = i
                    keep_j = j
        return prices[keep_j] - prices[keep_i]

                

