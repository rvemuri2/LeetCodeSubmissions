class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        l1, l2 = len(str1), len(str2)
        
        def GCD(i):
            
            if(l1 % i != 0 and l2 % i != 0):
                return False
            
            return str1[:i] * (l1 // i) == str1 and str1[:i] * (l2 // i) == str2
        
        for i in range(min(l1, l2), 0, -1):
            
            if GCD(i):
                
                return str1[:i]
            
        return ""
        
      
    
    
    
    
    