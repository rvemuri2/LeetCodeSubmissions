class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        
        count = 0
        h = {}
        
        
        for i in stones:
            h[i] = 1 + h.get(i, 0)
            
    
        for i in jewels: 
           
            if i in h:
                
                count += h[i]
                
                
        return count
            
        