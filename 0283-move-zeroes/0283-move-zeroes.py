class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        
        for i in range(len(nums)):
            if(nums[i] != 0):
                val = nums[i]
                nums.pop(i)
                nums.insert(count, val)
                count += 1
        
                
            
        