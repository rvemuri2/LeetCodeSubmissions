class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = 0
        
        h = {}
        
        for i in nums:

            h[i] = 1 + h.get(i, 0)
            
        
        for i in h:
            
            count += h[i] * (h[i] - 1)//2
            
        return count
        