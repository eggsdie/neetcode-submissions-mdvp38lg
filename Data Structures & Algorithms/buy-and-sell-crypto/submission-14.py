class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0 

        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                price = prices[r]-prices[l]
                total = max(total, price)
            else:
                l=r
            r+=1

        return total
