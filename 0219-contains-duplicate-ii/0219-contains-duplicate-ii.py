class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        h = set()
        j = 0
        
        for i in range(len(nums)):
            
            if(i - j > k):
                h.remove(nums[j])
                j += 1
            if(nums[i] in h):
                return True
            
            h.add(nums[i])
            
        
        return False