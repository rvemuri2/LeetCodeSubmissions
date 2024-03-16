class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        arr = []
        
        j = 0
        
        for i in pushed:
            
            arr.append(i)
            while(j < len(popped) and arr and arr[-1] == popped[j]):
                arr.pop()
                j+=1
        return not arr
        
                
                
                
            
            
        