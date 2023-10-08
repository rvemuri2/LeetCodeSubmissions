class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        l, total = 0, 0
        length = float("inf")
        
        for i in range(len(nums)):
            
            total += nums[i]
            
            while(total >= target):
                total -= nums[l]
                length = min(i - l + 1, length)
                l += 1
            
        return 0 if length == float("inf") else length
            
            
            
        