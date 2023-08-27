class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        arr = defaultdict(list)
        
        for i in strs:
            
            char = [0] * 26 #Character Array 
            
            for j in i:
                
                char[ord(j) - ord("a")] += 1
                
            
            arr[tuple(char)].append(i)
            print(arr[tuple(char)]) 
            
        return arr.values()