class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        counter = defaultdict(int)
        
       
                
        h = {}
        
        str1 = "balloon"
        
        for c in text:
            if c in str1:
                counter[c] += 1
            
        
        return min(counter['b'], counter['a'],counter['l']//2, counter['o']//2, counter['n'])