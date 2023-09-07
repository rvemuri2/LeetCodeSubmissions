class Solution(object):
    def containsDuplicate(self, nums):
        
        h = {}
        
        for i in nums:
            h[i] = 1 + h.get(i, 0)
            
        for i in h:
            if(h[i] > 1):
                return True
        
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        