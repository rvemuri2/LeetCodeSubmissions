class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        
        i = 0
        j = 1
        Lcount = 0
        Scount = 0
        while(i < len(nums) and j < len(nums)):
            
            if(nums[i] > nums[j]):
                
                Scount += 1
            
            if(nums[i] < nums[j]):
                
                Lcount += 1
        
            if(nums[i] == nums[j]):
                
                Scount += 1
                Lcount += 1
                
            j+=1
            i+=1
        
        
        if(Lcount == len(nums)-1 or Scount == len(nums)-1):
            return True
        else:
            return False
            
            
        