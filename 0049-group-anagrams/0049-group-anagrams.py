class Solution:
    def groupAnagrams(self, strs: List[str]):
    
        h = defaultdict(list)
        
        
        
        for i in strs:
            
            arr = [0] * 26
            
            for k in i:
                
                arr[ord(k) - ord("a")] += 1
              
                
            h[tuple(arr)].append(i)
        
        return h.values()
            
        
            
            