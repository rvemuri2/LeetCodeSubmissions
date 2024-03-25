class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        counter = defaultdict(int)
        
       
                
        h = {}
        
        str1 = "balloon"
        
        for c in text:
            if c in str1:
                counter[c] += 1
        
        print(counter)
        for i in str1:
            
            h[i] = 1 + h.get(i, 0)
            
        
        return min(counter['b'], counter['a'],counter['l']//2, counter['o']//2, counter['n'])