class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        arr = []
        
        for i in range(len(nums)):
            
            arr.append(i+1)
            
        
        
        for i in arr:
            
            if i not in nums:
                return i
        
        return 0
            
        
            
            
        