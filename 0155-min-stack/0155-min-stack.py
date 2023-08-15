class MinStack:
    

    def __init__(self):
        
        self.arr = []
        self.arr2 = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.number = min(val, self.arr2[-1] if self.arr2 else val)
        self.arr2.append(self.number)
       

    def pop(self) -> None:
        self.arr.pop()
        self.arr2.pop()
       
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.arr2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()