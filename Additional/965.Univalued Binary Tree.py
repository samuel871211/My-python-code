# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None:
            return False
        else:
            arr = []
            return haha().pre(root,arr)
            
class haha:
    def pre(self,root,arr):
        arr.append(root.val)
        if root.left is not None:
            haha().pre(root.left,arr)
        if root.right is not None:
            haha().pre(root.right,arr)
        if len(set(arr)) == 1:
            return True
        return False
