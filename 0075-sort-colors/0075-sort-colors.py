class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        c1, c2, c3 = 0, 0, 0
        
        for i in nums:
            
            if i == 0:
                c1 +=1
            
            if i == 1:
                c2 += 1
                
            if i == 2:
                c3 += 1
                
        
        for i in range(c1):
            
            nums[i] = 0
        
        for i in range(c2):
            
            nums[i + c1] = 1
            
        for i in range(c3):
            
            nums[i + c1 + c2] = 2
            
        
            
            
            