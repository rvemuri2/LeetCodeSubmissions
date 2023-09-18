class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        count = 0
        m1 = 0
        
        for i in gain: 
            
            count += i
            m1 = max(m1, count)
            
        
        return m1
        