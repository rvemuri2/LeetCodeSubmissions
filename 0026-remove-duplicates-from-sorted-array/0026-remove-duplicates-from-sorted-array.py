class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        i = 0
        j = 1
        while(j < len(nums)):
            if(nums[i] != nums[j]):
                count += 1
                i += 1
                nums[i] = nums[j]
                j+=1
                
            else:
                j += 1

            


        
        return count