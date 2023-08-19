class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        l1, l2 = len(str1), len(str2)
        
        def GCD(i):
            if(l1 % i and l2 % i):
                return False   
           
            return str2[:i] * (l2//i) == str2 and str2[:i] * (l1//i) == str1
                
        
        for i in range(min(l1, l2), 0, -1):
            
            if GCD(i):
                return str2[:i]
                
        return "" 
    
    
    
    