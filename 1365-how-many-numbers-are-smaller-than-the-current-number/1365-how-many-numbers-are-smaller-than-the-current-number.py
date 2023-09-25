class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Determine the maximum number in nums.
        max_num = max(nums)
        
        # Create a list to count the occurrences of each number in nums.
        count = [0] * (max_num + 1)
        
        # Count the occurrences of each number in nums.
        for num in nums:
            count[num] += 1
        
        # Calculate the number of elements smaller than each number.
        smaller_counts = [0] * (max_num + 1)
        smaller_sum = 0
        
        for i in range(max_num + 1):
            smaller_counts[i] = smaller_sum
            smaller_sum += count[i]
        
        # Create the result array based on the smaller counts.
        result = [0] * len(nums)
        for i, num in enumerate(nums):
            result[i] = smaller_counts[num]
        
        return result

            
            
        
        
            
            