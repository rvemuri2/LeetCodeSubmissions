class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
    
    
    
        num1, num2 = float("inf"), float("inf")
        
        for i in nums: 
            
            if(i <= num1):
                num1 = i
                
            elif(i <= num2):
                num2 = i
                
            else:
                return True
            
        
        return False
        