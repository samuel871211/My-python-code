# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        else: return self.helper(root,[])
    def helper(self,root,arr):
        if root.left: self.helper(root.left,arr)
        arr.append(root.val)
        if root.right: self.helper(root.right,arr)
        return arr
