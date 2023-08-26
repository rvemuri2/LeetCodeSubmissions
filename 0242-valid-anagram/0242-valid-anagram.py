class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h1 = {}
        h2 = {}
        
        if(len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            
            h1[s[i]] = 1 + h1.get(s[i], 0)
            h2[t[i]] = 1 + h2.get(t[i], 0)
            
        print("h1", h1)
        print("h2", h2)
        
        for j in h1: 
            
            if(h1[j] != h2.get(j)):
                return False
        
        return True
        
        
            
          
     
                
                
        