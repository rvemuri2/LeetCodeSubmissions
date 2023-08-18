class ListNode():
    def __init__(self, val, prev=None, next1=None):
        self.val = val
        self.prev = prev
        self.next = next1
class BrowserHistory(object):

    
    def __init__(self, homepage):
        self.curr = ListNode(homepage)
        """
        :type homepage: str
        """
        

    def visit(self, url):
        
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next
        
        """
        :type url: str
        :rtype: None
        """
        

    def back(self, steps):
        
        while(self.curr.prev != None and steps != 0):
            self.curr = self.curr.prev
            steps -= 1
        """
        :type steps: int
        :rtype: str
        """
        return self.curr.val
        

    def forward(self, steps):
        while(self.curr.next != None and steps != 0):
            self.curr = self.curr.next
            steps -= 1
        """
        :type steps: int
        :rtype: str
        """
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)