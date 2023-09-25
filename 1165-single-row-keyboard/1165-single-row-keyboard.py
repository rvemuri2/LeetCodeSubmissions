class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        h = {}
        count = 0
        l = 0 
        c = 0
        
        for i in keyboard: 
            
            h[i] = c
            c+=1
            
            
        
        for i in word: 
            
            count += abs((l-h[i]))
         
            l = h[i]
            
        return count
        