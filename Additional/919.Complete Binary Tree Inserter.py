# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class helper:
    def count(self,root,arr):
        if root == None:
            return len(arr) + 1
        else:
            arr.append(root.val)
            if root.left is not None:
                helper().count(root.left,arr)
            if root.right is not None:
                helper().count(root.right,arr)
            return len(arr) + 1

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.cur_index = helper().count(root,[])
       
    def insert(self, v: int) -> int:
        if self.root == None:
            self.root = TreeNode(v)
            return None
        else:
            if self.root.left == None:
                self.root.left = TreeNode(v)
                self.cur_index += 1 
                return self.root.val
            elif self.root.right == None:
                self.root.right = TreeNode(v)
                self.cur_index += 1 
                return self.root.val
            else:
                arr = []
                path = self.cur_index //2
                while path != 1:
                    arr.insert(0,path)
                    path = path // 2
                cur = self.root
                for i in range(len(arr)):
                    if arr[i] % 2 == 1:
                        cur = cur.right
                    else:
                        cur = cur.left
                if self.cur_index % 2 == 1:
                    cur.right = TreeNode(v)
                else:
                    cur.left = TreeNode(v)       
                self.cur_index += 1 
                return cur.val

    def get_root(self) -> TreeNode:
        return self.root
