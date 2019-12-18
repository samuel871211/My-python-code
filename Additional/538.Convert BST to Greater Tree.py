# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root == None or (root.left == None and root.right == None):
            return root
        else:
            self.sum = 0
            self.helper(root)
            return root
    
    def helper(self,root):
        if root.right:
            self.helper(root.right)
        
        self.sum += root.val
        root.val = self.sum
        
        if root.left:
            self.helper(root.left) 
