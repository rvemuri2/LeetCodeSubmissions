# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            
            if not root: return [True, 0] #We are returning if the tree is balanced and it's height
            
            left, right = dfs(root.left), dfs(root.right)
            
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1 #we get that this balanced if it's <= 1 based on it's determination
            
            return [balance, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
            
            