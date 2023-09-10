class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        p = []

        for i, a in enumerate(nums):

            if(i > 0 and a == nums[i-1]):
                continue


            y = i + 1
            z = len(nums) - 1

            while(y < z):
            
                sum1 = a + nums[y] + nums[z]

                if(sum1 > 0):
                    z-=1
                
                elif(sum1 < 0):
                    y+=1

                else:
                    p.append([a, nums[y], nums[z]] )
                    y+=1
                    while(nums[y] == nums[y-1] and y < z):
                        y+=1
                    

        return p




        