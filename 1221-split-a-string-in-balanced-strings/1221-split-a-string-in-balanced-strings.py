class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        countL = 0
        countR = 0
    
        count = 0
        for i in s: 

            if(i == "L"):
                
                countL += 1
                
                if(countL == countR):
                    
                    count += 1
                    
            
            if(i == "R"):
                
                countR += 1
                
                if(countL == countR):
                    
                    count+=1
                    
        
        return count
            
        