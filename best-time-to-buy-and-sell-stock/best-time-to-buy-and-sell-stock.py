class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        left,right = 0,1
        for i in range(0, len(prices)-1):
            maxProfit = max(maxProfit, prices[right]-prices[left])
            if prices[left]>prices[right]:
                left= right
            
            right = right + 1
        
        return maxProfit
                
        