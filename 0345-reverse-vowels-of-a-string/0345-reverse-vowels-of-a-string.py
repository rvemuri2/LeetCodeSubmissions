class Solution:
    def reverseVowels(self, s: str) -> str:
        
        i = 0
        j = len(s)-1
        
        arr = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        
        str2 = list(s)
        print(str2)
        
        str1=""
        
        while(i < j):
            if(str2[i] in arr and str2[j] in arr):
                temp = str2[i]
                str2[i] = str2[j]
                str2[j] = temp
                i+=1
                j-=1
            
            if(str2[i] in arr and str2[j] not in arr):
                j-=1
            
            if(str2[j] in arr and  str2[i] not in arr):
                i+=1
            
            if(not str2[j] in arr and not str2[i] in arr):
                i+=1
                j-=1
        
        for i in str2:
            str1+=i
                 
        
        return str1
        