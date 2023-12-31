class MinStack:
    

    def __init__(self):
        
        self.a = []
        self.min1 = []
        

    def push(self, val: int) -> None:
      
        self.a.append(val)
        n = min(val, self.min1[-1] if self.min1 else val)
        self.min1.append(n)
    

    def pop(self) -> None:
        self.a.pop()
        self.min1.pop()
       
        

    def top(self) -> int:
        return self.a[-1]


    def getMin(self) -> int:
        return self.min1[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()