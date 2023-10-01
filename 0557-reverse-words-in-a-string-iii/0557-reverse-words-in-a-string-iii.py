class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = list(s)
        
        l = 0
        
        for i in range(len(arr)):
            
            if(arr[i] == " " or i == len(arr)-1):
            
                tl, tr = l, i-1
                
                if(i == len(arr)-1):
                    tr = i
                    
                while(tl < tr):
                    arr[tl], arr[tr] = arr[tr], arr[tl]
                    tl += 1
                    tr -=1
                
                l = i + 1
                
                
        
        return "".join(arr)
        
        
        