class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        j = 0
        i = 1
        total = 0
        
        while(i < len(prices)):
            
            if(prices[i] > prices[j]):
                total = max(total, prices[i] - prices[j])
            else:
                j = i
            
            i+=1
            
        return total
        