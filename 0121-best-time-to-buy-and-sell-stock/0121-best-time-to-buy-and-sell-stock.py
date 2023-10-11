class Solution(object):
    def maxProfit(self, prices):
        l = 0
        total = 0
        least = float('inf')
        
        for i in range(1, len(prices)):
            least = min(least, prices[l])
            total = max(total, prices[i] - least)
            l+=1
            
        return total
        """
        :type prices: List[int]
        :rtype: int
        """
        