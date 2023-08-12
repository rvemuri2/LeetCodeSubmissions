class Solution:
    def isValid(self, s: str) -> bool:
        
        t = False
        
        h = {")": "(", "}":"{", "]":"["}
        
        arr = []
        
        
        for i in s:
            
            
            if(i == "(" or i == "{" or i == "["):  
                arr.append(i)
                
            if(i in h and len(arr) == 0):
                return False
                
            else:
                if(i in h and len(arr) > 0):
                    if(h.get(i) == arr[-1]):
                        arr.pop()
                    else:
                        return False
                       
        
        if(len(arr) == 0):
            return True
        else:
            return False
                    
        
                
                
                
            