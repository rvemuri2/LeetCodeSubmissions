class Solution(object):
    def containsDuplicate(self, nums):
        
        arr = set(nums)
        
        if(len(nums) == len(arr)):
            return False
        
        else:
            return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        