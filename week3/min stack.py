class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        self.stack.append((x, min(x, self.getMin())))
        

    def pop(self): #定義pop函數，用來取得stack最上面的值
        if len(self.stack)==0: return None #如果self.stack的長度=0，就return none
        return self.stack.pop()[0] #return self.stack最上面的值 [0]代表資料的第0個位置
        

    def top(self):
        if len(self.stack)==0: return None
        return self.stack[-1][0]
        

    def getMin(self):
        if len(self.stack)==0: return float('inf')
        return self.stack[-1][1]
