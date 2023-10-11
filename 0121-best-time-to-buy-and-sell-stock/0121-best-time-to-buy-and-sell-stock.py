class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        j = 0
        total = 0
        least = float('inf')
        for i in range(1, len(prices)):
            
            least = min(least, prices[j])
            total = max(total, prices[i] - least)
            j+=1
            
        return total
        