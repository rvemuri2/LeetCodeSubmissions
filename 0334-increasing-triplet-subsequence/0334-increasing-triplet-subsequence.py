class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n1, n2 = 100000000000, 100000000000
        
        for i in nums: 
            
            if(i <= n1):
                n1 = i
                
            elif(i <= n2):
                n2 = i
            
            else:
                return True
            
    
    
        return False
    
       
        