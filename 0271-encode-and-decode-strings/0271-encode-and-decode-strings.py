class Codec:
    
    def encode(self, strs: List[str]) -> str: 
        str1 = ""
        for i in strs:
            str1 += str(len(i)) + "?" + i
        
        return str1

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        
        while(i < len(s)):
            j = i
            while(s[j] != "?"):
                j+=1
            
            length = int(s[i:j])
            arr.append(s[j+1: j + 1 + length]) 
            i = j + length + 1
        
        return arr
       
                
        
        """Decodes a single string to a list of strings.
        """
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))