class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        total = 0
        min1 = float("inf")
        
        l = 0
        
        for i in range(len(nums)):
            
            total += nums[i]
            
            while(total >= target):
                
                total -= nums[l]
                min1 = min(i - l + 1, min1)
                l+=1
                
        return 0 if min1 == float('inf') else min1
        
        
        
        
        
#         l, total = 0, 0
#         length = float("inf")
        
#         for i in range(len(nums)):
            
#             total += nums[i]
            
#             while(total >= target):
#                 total -= nums[l]
#                 length = min(i - l + 1, length)
#                 l += 1
            
#         return 0 if length == float("inf") else length