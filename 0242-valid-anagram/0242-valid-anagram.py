class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        h1 = {}
        h2 = {}
        
        if(len(s) != len(t)):
            return False
        
        else:
            
            for i in s: 
                
                h1[i] = 1 + h1.get(i, 0)
                
            for i in t:
                
                h2[i] = 1 + h2.get(i, 0)
                
        
            
            for i in h1:
                
                if h1[i] != h2.get(i):
                    return False
                
            return True
            
            
        