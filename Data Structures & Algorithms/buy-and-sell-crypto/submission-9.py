class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        total = 0

        while (r < len(prices)):
            if prices[l] < prices[r]:
                curMax = prices[r] - prices[l]
                total = max(total, curMax)
            else:
                l=r
            r+=1

        return total
