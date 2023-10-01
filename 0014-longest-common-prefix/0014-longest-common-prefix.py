class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        str1 = ""
        
        for i in range(len(strs[0])):
            
            for j in strs[1:]:
                
                if(i == len(j) or j[i] != strs[0][i]):
                    return str1
                
                
                print(j[i])
            print("hi")
            str1 += strs[0][i]
            
        return str1
                
                
        