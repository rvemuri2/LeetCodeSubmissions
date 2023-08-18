class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        j = 0
        
        arr = []
        
        while(i < len(word1) or j < len(word2)):
            
            if(i < len(word1)):   
                arr.append(word1[i])
                i+=1
            
            if(j < len(word2)):
                arr.append(word2[j])
                j+=1
            
        str1 = ""
        
        for i in arr:
            str1 += i
        
        return str1
        