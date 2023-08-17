class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        arr = []
        sum2 = 0
        
        for i in operations:
            
            if(i.isnumeric and i != "+" and i != "D" and i != "C"):
                
                arr.append(int(i))
                
            elif(i == "C"):
                arr.pop()
                
            elif(i == "D"):
                arr.append(int(arr[-1]) * 2)
                
            elif(i == "+"):
                sum1 = int(arr[-1]) + int(arr[len(arr) - 2])
                arr.append(sum1)
                
            
        
        for i in arr:
            
            sum2 += i
            
        return sum2
      
       
            