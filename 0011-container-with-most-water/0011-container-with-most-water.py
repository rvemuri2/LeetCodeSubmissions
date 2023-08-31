class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        
        i = 0
        j = len(height) - 1
        
        while(j != i):
            
            if(height[j] <= height[i]):
                
                area = max(area, height[j] * (j - i))   
                j-=1
            
            if(height[j] > height[i]):
                area = max(area, height[i] * abs((j - i)))  
                i+=1
            
        return area