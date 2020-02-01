# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        return self.helper(root,[])
        
    def helper(self,root,arr):
        arr.append(root.val)
        if root:
            if root.left:
                self.helper(root.left,arr)
            if root.right:
                self.helper(root.right,arr) 
        return arr
