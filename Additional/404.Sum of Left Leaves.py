# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None or (root.left == None and root.right == None):
            return 0
        else:
            self.leftsum = 0
            self.det = None
            self.helper(root)
            return self.leftsum
    
    def helper(self,root):
        if root.left:
            self.det = True
            self.helper(root.left)
        if root.right:
            self.det = False
            self.helper(root.right)
        if root.right == None and root.left == None:
            if self.det:
                self.leftsum += root.val
