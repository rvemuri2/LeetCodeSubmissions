class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        h = set(nums)
        count = 0
        
        
        
        for i in h:
            if(i - 1 not in h):
                length = 0
                while(i + length in h):
                    length += 1
                    count = max(count, length)
                
                
          
        return count
            
                
     
            
        