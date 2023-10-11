class Solution(object):
    def maxProfit(self, prices):
      
        total = 0
        least = float('inf')
        
        for i in prices:
            least = min(least, i)
            total = max(total, i - least)
           
            
        return total
        """
        :type prices: List[int]
        :rtype: int
        """
        