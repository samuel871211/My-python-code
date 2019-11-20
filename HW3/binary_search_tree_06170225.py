class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def insert(self,root,val):
        if root == None:
            NewNode = TreeNode(val)
            return NewNode
        elif root.val == val:
            NewNode = TreeNode(val)
            NewNode.left = root.left
            root.left = NewNode
            return NewNode
        elif root.val < val: #往右邊
            if root.right == None: #右邊沒小孩，直接給Node
                root.right = TreeNode(val)
                return root.right
            else: #右邊有小孩，recursive
                return Solution().insert(root.right,val)
        else: #往左邊
            if root.left == None: #左邊沒小孩，直接給Node
                root.left = TreeNode(val)
                return root.left
            else: #左邊有小孩，recursive
                return Solution().insert(root.left,val)
    
    def search(self,root,target):
        if root.val == target:
            return root
        elif root.val > target: #往左邊 
            if root.left == None: #左邊空
                return None
            else: #左邊不空，recursive
                root = root.left
                return Solution().search(root,target)
        else: #往右邊
            if root.right == None: #右邊空
                 return None
            else: #右邊不空，recursive
                root = root.right
                return Solution().search(root,target)
    
    def pre(self,root,arr):
        if root == None:
            return arr
        else:
            arr.append(root.val)
            if root.left is not None:
                Solution().pre(root.left,arr)
            if root.right is not None:
                Solution().pre(root.right,arr)
            return arr
    
    def modify(self,root,target,new_val):
        if target is not new_val:       
            Solution().insert(root,new_val)
            return Solution().delete(root,target)
        else:
            return root
        
    def delete(self,root,target):
        
        if root.val == target:
            
            # 有重複值的情況，把重複值弄成一個
            
            d = root
            while d.left is not None and d.left.val == target:
                d = d.left
            root.left = d.left
            
            # case 5: root底下沒有小孩
            
            if root.left is None and root.right is None:
                root = None
                return None
            
            # case 6: root底下只有左小孩
            
            elif root.left is not None and root.right is None:
                n = root.left
                root = None
                return n
            
            # case 7: root底下只有右小孩
            
            elif root.right is not None and root.left is None:
                n = root.right
                root = None
                return n
            
            #case 8: root底下有兩個小孩
            
            elif root.left is not None and root.right is not None:
                
                #case 8-1: 不需要找左subtree最大 or 右subtree最小
                
                if root.left.right is None and root.right.left is None:
                    n = root.left
                    n.right = root.right
                    root = None
                    return n                        
                
                #case 8-2: 找右subtree最小
                
                elif root.left.right is None and root.right.left is not None:
                    tp = root.right
                    t = root.right.left
                    while t.left is not None:
                        tp = t
                        t = t.left
                    if root.right == tp:
                        tp.left = t.right
                        t.right = root.right
                        t.left = root.left
                        root = t
                    else:
                        tp.left = t.right
                        t.right = root.right
                        t.left = root.left
                        root = t
                    return root
                
                #case 8-3: 找左subtree最大
                
                elif root.left.right is not None:
                    tp = root.left
                    t = root.left.right
                    while t.right is not None:
                        tp = t
                        t = t.right
                    if root.left == tp:
                        tp.right = t.left
                        t.left = root.left
                        t.right = root.right
                        root = t
                    else:
                        tp.right = t.left
                        t.right = root.right
                        t.left = root.left
                        root = t
                    return root
        
        else:
            
            # 僅先找到 "刪除節點" 跟 "刪除節點的parent"，還未考慮重複值的問題
            
            p = None
            dr = root       
            while dr is not None and dr.val != target:
                if target > dr.val: #往右邊
                    if dr.right is None:
                        return root
                    else:
                        p = dr
                        dr = dr.right
                else:
                    if dr.left is None:
                        return root
                    else:
                        p = dr
                        dr = dr.left
                        
            # 有重複值的情況，把重複值弄成只有一個
            d = dr
            while d.left is not None and d.left.val == target:
                d = d.left
            if p.left is not None and p.left.val == dr.val:
                p.left = d
            else:
                p.right = d
            d.right = dr.right

            # case 1: 刪除節點 只有左小孩
            
            if d.left is not None and d.right is None:
            
                #case 1-1: 刪除節點的左小孩底下 沒有右小孩
                
                if d.left.right is None:
                    if p.left is not None and p.left.val == d.val:
                        p.left = d.left
                    else:
                        p.right = d.left
                    d = None
                    return root
            
                #case 1-2: 刪除節點的左小孩底下 有右小孩
                
                else:               
                    tp = d.left
                    t = d.left.right
                    while t.right is not None:
                        tp = t
                        t = t.right
                    
                    if d.left.val == tp.val:
                        if p.left is not None and p.left.val == d.val:
                            p.left = t
                        else:
                            p.right = t
                        tp.right = t.left  
                        t.left = d.left
                    else:
                        if p.left is not None and p.left.val == d.val:
                            p.left = t
                        else:
                            p.right = t
                        tp.right = t.left
                        t.left = d.left
                    d = None
                    return root
            
            # case 2: 刪除節點 只有右小孩
            
            elif d.left is None and d.right is not None:
                
                #case 2-1: 刪除節點的右小孩底下 沒有左小孩
            
                if d.right.left is None:
                    if p.left is not None and p.left.val == d.val:
                        p.left = d.right
                    else:
                        p.right = d.right
                    d = None
                    return root
                    
                #case 2-2: 刪除節點的右小孩底下 有左小孩
                
                else:
                    tp = d.right
                    t= d.right.left
                    while t.left is not None:
                        tp = t
                        t = t.left
                    
                    if d.right.val == tp.val:
                        if p.left is not None and p.left.val == d.val:
                            p.left = t
                        else:
                            p.right = t
                        tp.left = t.right
                        t.right = d.right                    
                    else:
                        if p.left is not None and p.left.val == d.val:
                            p.left = t
                        else:
                            p.right = t
                        tp.left = t.right
                        t.right = d.right
                    d = None
                    return root
                        
            # case 3: 刪除節點 有兩個小孩
            
            elif d.left is not None and d.right is not None:
                
                #case 3-1: 刪除節點的 left.right 跟 right.left 皆為空
                
                if d.left.right is None and d.right.left is None:
                    if p.left is not None and p.left.val == d.val:
                        p.left = d.left
                    else:
                        p.right = d.left
                    d.left.right = d.right
                    d = None
                    return root
                
                #case 3-2: 刪除節點的 left.right存在
                
                elif d.left.right is not None:
                    tp = d.left
                    t = d.left.right
                    while t.right is not None:
                        tp = t
                        t = t.right
                    
                    if d.left.val == tp.val:
                        if p.left is not None and p.left.val == d.val:
                            p.left = t
                        else:
                            p.right = t
                        tp.right = t.left
                        t.left = d.left
                        t.right = d.right                
                    else:
                        if p.left is not None and p.left.val == d.val:
                            p.left = t
                        else:
                            p.right = t
                        tp.right = t.left
                        t.left = d.left
                        t.right = d.right
                    d = None
                    return root
                
                #case 3-3: 刪除節點的 right.left存在 且 left.right不存在
                
                elif d.right.left is not None and d.left.right is None:
                    tp = d.right
                    t = d.right.left
                    while t.left is not None:
                        tp = t
                        t = t.left
                    
                    if d.right.val == tp.val:
                        if p.left is not None and p.left.val == d.val:
                            p.left = t
                        else:
                            p.right = t
                        tp.left = t.right
                        t.right = d.right
                        t.left = d.left                 
                    else:
                        if p.left is not None and p.left.val == d.val:
                            p.left = t
                        else:
                            p.right = t
                        tp.left = t.right
                        t.left = d.left
                        t.right = d.right
                    d = None  
                    return root
       
            #case 4: 刪除的節點 沒有小孩
            
            elif d.left is None and d.right is None:
                if p.left is not None and p.left.val == d.val:
                    p.left = None
                else:
                    p.right = None
                return root
