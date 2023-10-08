class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        arr = []
        
        m = 0
        
        l = 0
        
        for i in range(len(s)):
            
            while(s[i] in arr):
                arr.remove(s[l])
                l+=1
                
            
            arr.append(s[i])
            m = max(m, i - l + 1)
            
        return m
            
            
            