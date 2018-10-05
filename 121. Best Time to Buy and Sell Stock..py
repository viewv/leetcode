class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sellPrice = 9999999
        length = len(prices)
        maxAns = 0
        for x in range(0, length):
            if prices[x] < sellPrice:
                sellPrice = prices[x]
            if prices[x] > sellPrice:
                temp = prices[x] - sellPrice
                if temp > maxAns:
                    maxAns = temp
        return maxAns
