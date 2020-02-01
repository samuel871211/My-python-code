# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None or (root.left == None and root.right == None):
            return True
        else:
            if root.left != None and root.right != None:
                if self.helper(root.left,root.right) == False:
                    return False
                else:
                    return True
            else:
                return False
    
    def helper(self,r1,r2):
        if r1.val != r2.val:
            return False
        else:
            if r1.left != None and r2.right != None:
                if self.helper(r1.left,r2.right) == False:
                    return False
            elif r1.left == None and r2.right != None:
                return False
            elif r1.left != None and r2.right == None:
                return False
         
            if r1.right != None and r2.left != None:
                if self.helper(r1.right,r2.left) == False:
                    return False
            elif r1.right == None and r2.left != None:
                return False
            elif r1.right != None and r2.left == None:
                return False
