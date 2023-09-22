class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        h = {}
        arr = []
        m = 0
        for i in nums:
            
            h[i] = 1 + h.get(i, 0)
            arr.append(max(h, key=h.get))
        
        print(h)
        return arr[-1]
        
        
        
            
        