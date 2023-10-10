class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        arr = []
        l = 0
        
        m = 0
        
        for i in range(len(s)):
            
            while(s[i] in arr):
                arr.remove(s[l])
                l+=1
                
                
            arr.append(s[i])
            m = max(m, (i - l + 1))
           
            
        return m
        """
        :type s: str
        :rtype: int
        """
        