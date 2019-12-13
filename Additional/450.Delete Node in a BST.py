# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        elif root.val == key:
            if root.left == None and root.right == None:
                root = None
                return root
            elif root.left != None and root.right == None:
                root = root.left
                return root
            elif root.right != None and root.left == None:
                root = root.right
                return root
            else:
                if root.left.right == None and root.right.left == None:
                    root.left.right = root.right
                    root = root.left
                    return root
                elif root.left.right != None and root.right.left == None:
                    curp = root.left
                    cur = root.left.right
                    while cur.right != None:
                        curp = cur
                        cur = cur.right
                    curp.right = cur.left
                    cur.left = root.left
                    cur.right = root.right
                    root = cur
                    return root
                else:
                    curp = root.right
                    cur = root.right.left
                    while cur.left != None:
                        curp = cur
                        cur = cur.left
                    curp.left = cur.right
                    cur.left = root.left
                    cur.right = root.right
                    root = cur
                    return root
        else:
            curp = None
            cur = root
            while cur != None and cur.val != key:
                if cur.val > key:
                    if cur.left == None:
                        return root
                    else:
                        curp = cur
                        cur = cur.left
                elif cur.val < key:
                    if cur.right == None:
                        return root
                    else:
                        curp = cur
                        cur = cur.right
            else:
                if cur.left == None and cur.right == None:
                    if curp.right == cur:
                        curp.right = None
                    else:
                        curp.left = None
                    return root
                elif cur.left != None and cur.right == None:
                    if curp.right == cur:
                        curp.right = cur.left
                    else:
                        curp.left = cur.left
                    return root
                elif cur.left == None and cur.right != None:
                    if curp.right == cur:
                        curp.right = cur.right
                    else:
                        curp.left = cur.right
                    return root
                else:
                    if cur.left.right == None and cur.right.left == None:
                        cur.left.right = cur.right
                        if curp.right == cur:
                            curp.right = cur.left
                        else:
                            curp.left = cur.left
                        return root
                    elif cur.left.right != None and cur.right.left == None:
                        tp = cur.left
                        t = cur.left.right
                        while t.right != None:
                            tp = t
                            t = t.right
                        tp.right = t.left
                        if curp.right == cur:
                            curp.right = t
                            t.left = cur.left
                            t.right = cur.right
                        else:
                            curp.left = t
                            t.left = cur.left
                            t.right = cur.right
                        return root
                    else:    
                        tp = cur.right
                        t = cur.right.left
                        while t.left != None:
                            tp = t
                            t = t.left
                        tp.left = t.right
                        if curp.right == cur:
                            curp.right = t
                            t.left = cur.left
                            t.right = cur.right
                        else:
                            curp.left = t
                            t.left = cur.left
                            t.right = cur.right
                        return root
