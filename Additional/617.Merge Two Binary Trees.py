# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return t2
        if not t2: return t1
        self.helper(t1,t2)
        return t1
        
    def helper(self,t1,t2):
        t1.val = t1.val + t2.val
        
        if t1.left and t2.left:
            self.helper(t1.left,t2.left)
        elif not t1.left and t2.left:
            t1.left = t2.left
        
        if t1.right and t2.right:
            self.helper(t1.right,t2.right)
        elif not t1.right and t2.right:
            t1.right = t2.right
