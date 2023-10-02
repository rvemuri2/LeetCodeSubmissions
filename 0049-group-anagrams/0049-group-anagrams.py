class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        h = defaultdict(list)
        
        for i in strs:
            
            arr = [0] * 26
            
            for j in i: 
                
                arr[ord(j) - ord("a")] += 1
                
            
            h[tuple(arr)].append(i)
            
        return h.values()
        
        
        