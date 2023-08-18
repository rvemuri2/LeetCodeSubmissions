class MyStack:

    def __init__(self):
        
        self.arr = deque()
        

    def push(self, x: int) -> None:
        
        self.arr.append(x)
        

    def pop(self) -> int:
        
        for i in range(0, len(self.arr) - 1):
            
            self.arr.append(self.arr.popleft())
            
        return self.arr.popleft()
        

    def top(self) -> int:
        
        return self.arr[-1]
        

    def empty(self) -> bool:
        
        if(len(self.arr) == 0):
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()