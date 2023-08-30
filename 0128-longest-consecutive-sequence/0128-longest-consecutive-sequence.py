class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        
       
            
        print(h)
        
        count = 0
        length = 0
   
        for i in nums:
            if(i - 1 not in h):
                length = 0
                while(i + length in h):
                    length += 1
                count = max(count, length)
                
                
        return count
            
            
        