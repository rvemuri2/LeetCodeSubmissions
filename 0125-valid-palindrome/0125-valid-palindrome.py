class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        arr = []
        
        str1 = ""
        for i in s:
            if(i.isalnum()):
                arr.append(i)
        
        
                
        for i in arr:
            str1 += i
            
        str1 = str1.lower()
       
    
        i = 0
        j = len(str1) - 1
        
        while(j > i):
            if(str1[j] != str1[i]):
                return False
            
            j-=1
            i+=1
        
        return True
        
                
        