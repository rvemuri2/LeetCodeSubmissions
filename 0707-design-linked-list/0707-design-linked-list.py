class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:
    

    def __init__(self):
        self.right = Node(0)
        self.left = Node(0)
        self.right.prev = self.left
        self.left.next = self.right
        
        

    def get(self, index: int) -> int:
        
        curr = self.left.next
        while(curr != None and index > 0):
            curr = curr.next
            index -= 1
        if(curr != None and curr != self.right and index == 0):
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        node, next1, prev = Node(val), self.left.next, self.left
        prev.next = node
        next1.prev = node
        node.next = next1
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        node, next1, prev = Node(val), self.right, self.right.prev
        prev.next = node
        next1.prev = node
        node.next = next1
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while(curr != None and index > 0):
            curr = curr.next
            index -= 1
        
        if(curr != None and index == 0):
            node, next1, prev = Node(val), curr, curr.prev
            prev.next = node
            next1.prev = node
            node.next = next1
            node.prev = prev
            
    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while(curr != None and index > 0):
            curr = curr.next
            index -= 1
        
        if(curr != None and curr != self.right and index == 0):
            next1, prev = curr.next, curr.prev
            next1.prev = prev
            prev.next = next1
            
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)