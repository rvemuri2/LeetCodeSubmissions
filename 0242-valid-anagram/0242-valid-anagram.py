class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = 0
        
        if(len(s) != len(t)):
            return False
        
        
        arr = sorted(s)
        arr2 = sorted(t)
        
        for i in range(len(s)):
            if(arr[i] == arr2[i]):
                count += 1
       
           
        if(count == len(s)):
            return True
        else:
            return False