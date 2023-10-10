class Solution(object):
    def characterReplacement(self, s, k):
        
        total = 0
        h = {}
        l = 0
        
        for i in range(len(s)):
            h[s[i]] = 1 + h.get(s[i], 0)
            
            while((i - l + 1) - max(h.values()) > k):
                
                h[s[l]] -= 1
                l+=1
            
            total = max(total, (i - l + 1))
            
        return total
                
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        