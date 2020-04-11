class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        length = len(prices)
        for x in range(1, length):
            if prices[x] > prices[x - 1]:
                ans += prices[x] - prices[x - 1]
        return ans
