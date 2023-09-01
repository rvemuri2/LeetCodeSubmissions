class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        x = 0
        finalnums = []
        nums.sort() 
        
       
        
    
    
        
        prev = 1
       
        for x in range(0,len(nums)):
            
            if nums[x] == prev:
                #print("Got here")
                continue
                
            
            firstNum = nums[x]
            
            left = x+1
            right = len(nums) -1
            
            
 
            while left < right:
        
                total = nums[right] + nums[left] + firstNum
                  
                if  total < 0:
                    left = left + 1
                elif total > 0:
                    right = right -1
                else:
                    finalnums.append([firstNum,nums[left],nums[right]])
                    left = left + 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1
            prev = firstNum
                
        return finalnums
                    
        
                
                
        
        
        