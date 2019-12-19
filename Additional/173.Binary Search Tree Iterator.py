# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = self.pre(root,[])

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.arr:
            a = self.arr.pop(0)
            return a
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.arr:
            return True
        return False
    
    def pre(self,root,arr):
        if root == None:
            return arr
        else:
            if root.left:
                self.pre(root.left,arr)
            arr.append(root.val)
            if root.right:
                self.pre(root.right,arr)
        return arr
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
