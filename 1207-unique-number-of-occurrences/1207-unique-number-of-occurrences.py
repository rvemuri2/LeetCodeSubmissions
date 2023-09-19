class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        
        h = {}
        
        for i in arr: 
            
            h[i] = 1 + h.get(i, 0)
            
    
        
        s = set(h.values())
        print(s)
        print(len(h.values()))
        
        if(len(s) == len(h.values())):
            return True
        
        elif(len(s) != len(h.values())):
            return False
        
       

            
        
    
            
                
            
        
        