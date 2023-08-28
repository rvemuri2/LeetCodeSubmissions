class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash1 = defaultdict(list)
        
        for i in strs:
            
            arr = [0] * 26
            
            for c in i:
                
                arr[ord(c) - ord("a")] += 1
                
        
            hash1[tuple(arr)].append(i)
            
        return hash1.values()
            
        
            
            