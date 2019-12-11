# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            new = TreeNode(val)
            return new
        else:
            Solution().insert(root,val)
            return root
    def insert(self,root,val):
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                Solution().insert(root.right,val)
        else:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                Solution().insertIntoBST(root.left,val)
