class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        arr = set()
        max1 = 0
        
        l = 0
        
        for i in range(len(s)):
            while(s[i] in arr):
                arr.remove(s[l])
                l+=1
            
            arr.add(s[i]) 
            max1 = max(max1, i - l + 1)
        
        return max1
            
            