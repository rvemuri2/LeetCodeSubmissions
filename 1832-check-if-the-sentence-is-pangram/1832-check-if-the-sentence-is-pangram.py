class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        
        h = {}
        count = 0
        
        for i in sentence:
            
            h[i] = 1 + h.get(i, 0)
            
        
        for i in h.keys():
            
            count +=1
        
        if(count == 26):
            return True
        else:
            return False
        