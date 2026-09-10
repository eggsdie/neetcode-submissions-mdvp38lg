class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0 

        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l+=1

            price = prices[r]-prices[l]
            total = max(total, price)
            r+=1

        return total
