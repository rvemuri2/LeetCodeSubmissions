class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        c = defaultdict(int)
        
        count = 0
        
        h = {}
        c1 = 0
        
        print(c)
        for i in nums:
            c1 += c[i]
            c[i] += 1
            print(c1)

            h[i] = 1 + h.get(i, 0)
            
        
        for i in h:
            
            count += h[i] * (h[i] - 1)//2
            
        return count
        