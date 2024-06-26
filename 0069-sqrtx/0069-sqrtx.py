class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        l, r = 1, x-1
        
        while l <= r:
            
            m = (l + r)//2
            
            num = m * m
            
            if num > x:
                
                r = m - 1
                
            elif num < x:
                
                l = m + 1
                
            else:
                return m
            
        return r
        