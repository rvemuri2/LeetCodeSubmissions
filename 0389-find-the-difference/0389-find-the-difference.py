class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
        c1, c2 = Counter(s), Counter(t)
        
        print("c1", c1)
        print("c2", c2)
        
        
        for i in c2:
            
            if i not in c1:
                return i
            
            elif c1[i] < c2[i] or c2[i] < c1[i]:
                return i
            
            
       