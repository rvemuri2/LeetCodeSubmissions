class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        l1, l2 = len(str1), len(str2)
        
        def GCD(i):
            if(l1 % i and l2 % i):
                return False   
            f1, f2 = l1 // i, l2 // i
            return str2[:i] * f2 == str2 and str2[:i] * f1 == str1
                
        
        for i in range(min(l1, l2), 0, -1):
            
            if GCD(i):
                return str2[:i]
                
        return "" 
    
    
    
    