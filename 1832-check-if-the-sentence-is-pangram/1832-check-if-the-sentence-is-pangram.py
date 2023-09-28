class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        
        h = {}
        count = 0
        
        for i in sentence:
            
            h[i] = 1 + h.get(i, 0)
            
        
        return len(h) == 26
        