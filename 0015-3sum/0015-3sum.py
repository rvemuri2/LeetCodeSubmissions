class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        finalnums = []
        nums.sort() 
        
        prev = 1
       
        for x, a in enumerate(nums):
            
            if x > 0 and a == nums[x - 1]:
                continue
                
            
            firstNum = nums[x]
            
            left = x+1
            right = len(nums) -1
            
            
 
            while left < right:
        
                total = nums[right] + nums[left] + firstNum
                  
                if  total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    finalnums.append([firstNum,nums[left],nums[right]])
                    left+=1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1 
            prev = firstNum
                
        return finalnums
                    
        
                
                
        
        
        