class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = []
        
        for i in range(len(nums)):
            
            
            num = target - nums[i]
            
            if(num in arr):
                return [i, arr.index(target - nums[i])]
            
            arr.append(nums[i])
            
        
    
        