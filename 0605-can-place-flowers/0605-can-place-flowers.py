class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        count = 0
        for i in range(len(flowerbed)):
            
            if(flowerbed[i] == 0):
                
                
                
                prev = (i == 0 or flowerbed[i - 1] == 0)
                 
                next1 = ((i == len(flowerbed)-1) or flowerbed[i+1] == 0)
                  
                    
                if(prev and next1):
            
                    count += 1
                    flowerbed[i] = 1
                    if(count >= n):
                        return True
                    
                    
                    
                
                
            
       
        return count >= n
                
            
            
                
            
            
                
        
                
                
                
            
            
            
        