class Solution(object):
    def productExceptSelf(self, nums):
        
        prefix = [1] * len(nums)
        
        val = 1
        for i in range(len(nums)):
        
           
            prefix[i] = val
            val *= nums[i]
            
        post = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= post
            post *= nums[i]
            
            
        return prefix
            
            
       
        