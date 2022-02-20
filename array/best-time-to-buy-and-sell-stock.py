class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        O(n) solution scans through and stores minimum so far
        """
        
        min_ind = 0
        max = 0
        
        for i in range(len(prices)):
            if prices[i] < prices[min_ind]:
                min_ind = i
            
            if prices[i] - prices[min_ind] > max:
                max = prices[i] - prices[min_ind]
                
        return max
