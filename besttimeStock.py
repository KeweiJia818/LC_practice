class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) < 2:
        	return 0

        minprice = prices[0]
        profit = 0
        for i in range(0, len(prices)):
        	minprice = min(prices[i], minprice)
        	profit = max(profit, prices[i] - minprice)
        return profit