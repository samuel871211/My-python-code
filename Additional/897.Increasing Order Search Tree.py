# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root == None or (root.left == None and root.right == None):
            return root
        else:
            arr = self.traversal(root,[])
            new = TreeNode(arr[0])
            cur = new
            for i in range(1,len(arr)):
                cur.right = TreeNode(arr[i])
                cur = cur.right
            return new 
    
    def traversal(self,root,arr):
        if root.left:
            self.traversal(root.left,arr)
        arr.append(root.val)
        if root.right:
            self.traversal(root.right,arr)
        return arr
