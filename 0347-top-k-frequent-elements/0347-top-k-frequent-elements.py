class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        h = {}
        arr = []
        
        for i in nums:
            
            h[i] = 1 + h.get(i, 0) 
            
         
        print(h)
        
        for i in range(k):
            val = max(h.values())
            arr.append((list(h.keys())[list(h.values()).index(val)]))
            h.pop((list(h.keys())[list(h.values()).index(val)]))
            
        
        return arr
        
        
        if(len(nums) == 1):
            return [nums[0]]