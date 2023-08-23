class Solution(object):
    def productExceptSelf(self, nums):
        arr = [1] * len(nums)
        
        p = 1
        for i in range(len(nums)):
            arr[i] = p
            p *= nums[i]
            
        o = 1
        for i in range(len(nums) - 1, -1, -1):
            arr[i] *= o
            o *= nums[i]
            
        return arr
        