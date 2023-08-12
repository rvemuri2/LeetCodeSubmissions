class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        arr = []
        sum1 = 0
        for i in range(0, len(operations)):
            if(operations[i].isnumeric() or (operations[i] != "C" and operations[i] != "D" and operations[i] != "+") ):
                arr.append(int(operations[i]))
                
            if(operations[i] == "C"):
                arr.pop()
                
            if(operations[i] == "D"):
                arr.append(int(arr[-1] * 2))
   
                
            if(operations[i] == "+"):
                arr.append(int(arr[-1]) + int(arr[len(arr) - 2]))
                
        
        for i in arr:
            sum1 += i
            print(i)
            
        return sum1
            