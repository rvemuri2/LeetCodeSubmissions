class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = []
        
        for i in range(len(nums)):
            
            
            if(target-nums[i] in arr):
                return [i, arr.index(target - nums[i])]
            
            arr.append(nums[i])
            
        
    
        