class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        j = 0
        i = 1
        total = 0
        least = float('inf')
        while(i < len(prices)):
            
            least = min(least, prices[j])
            total = max(total, prices[i] - least)
            j+=1
            i+=1
            
        return total
        