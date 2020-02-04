# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = self.in_order(root,[])
        return arr[k-1]
    
    def in_order(self,root,arr):
        if root:
            if root.left:
                self.in_order(root.left,arr)
            arr.append(root.val)
            if root.right:
                self.in_order(root.right,arr)
        return arr
