class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        
        
        count = 0
        c = 0
        for i in sentences: 
            
            for j in i: 
                
                if j == " ":
                    c+= 1
                
            count = max(count, c)
            c = 0
            
        
        return count+1
        