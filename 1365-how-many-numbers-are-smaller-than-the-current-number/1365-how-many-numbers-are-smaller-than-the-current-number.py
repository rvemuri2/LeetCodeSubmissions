class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        
       
        
        arr = sorted(nums)
        
        arr2 = [1] * len(nums)
        
        for i in range(len(nums)):
            
            arr2[i] = arr.index(nums[i])
            
            
        
        return arr2
            
            
        
        
            
            