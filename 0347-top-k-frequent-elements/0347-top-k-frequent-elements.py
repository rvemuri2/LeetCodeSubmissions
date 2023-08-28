class Solution(object):
    def topKFrequent(self, nums, k):
        h = {}
        f = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            h[i] = 1 + h.get(i, 0)
            
        for i, j in h.items():
            f[j].append(i)
            
        r = []
        
        for i in range(len(f) - 1, 0, -1):
            for n in f[i]:
                r.append(n)
                if(len(r) == k):
                    return r
        