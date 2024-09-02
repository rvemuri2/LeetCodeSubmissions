# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if(not p and not q): #Both null
            return True
        
        if(not p or not q): #one is not null, one null
            return False
        
        if(p.val != q.val): #Val not equal to each other
            return False
            
    
            
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        