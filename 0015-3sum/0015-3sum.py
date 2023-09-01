class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        a=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    b=[nums[i],nums[l],nums[r]]
                    if b not in a:
                        a.append(b)
                    l+=1               
        return a
                    
        
                
                
        
        
        