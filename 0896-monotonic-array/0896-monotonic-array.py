class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        Lcount = 0
        Scount = 0
        for i in range(len(nums)-1):
            
            if(nums[i] > nums[i+1]):
                
                Scount += 1
            
            elif(nums[i] < nums[i+1]):
                
                Lcount += 1
        
            else:
                
                Scount += 1
                Lcount += 1
            
        
        
        if(Lcount == len(nums)-1 or Scount == len(nums)-1):
            return True
        else:
            return False
            
            
        