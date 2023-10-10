class Codec:

    def encode(self, strs):
        str1 = ""
        for i in strs:
            
            str1 += str(len(i)) + "?" + i
            
        return str1
            
            
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        

    def decode(self, s):
        arr = []
        i = 0
        
        while(i < len(s)):
            j = i
            while(s[j] != "?"):
                j+=1
                
            l = int(s[i:j])
            arr.append(s[j+1: j + l + 1])
            i = j + l + 1
            
        
        return arr
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
       
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))