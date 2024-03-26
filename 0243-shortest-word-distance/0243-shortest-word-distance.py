class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        
        l1, l2 = -1, -1
        
        dist = float('inf')
        
        for i in range(len(wordsDict)):
            
            if(wordsDict[i] == word1):
                l1 = i 
                
            if(wordsDict[i] == word2):
                l2 = i
                
            
            if(l1 != -1 and l2 != -1):
                
                dist = min(dist, abs(l2 - l1))
                
        return dist
        
        
                
                
            
            
        