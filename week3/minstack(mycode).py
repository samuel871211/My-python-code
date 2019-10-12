class MinStack(object):

    def __init__(self):
        self.main=[] #總共創造兩個[]，main用來存放所有push進來的資料
        self.mins=[] #當push值進來時，mins用來存放最小值    

    def push(self, x):
        self.main.append(x)                         #沒有任何懸念，push值就直接append進self.main
        if len(self.main) == 1 or x<=self.mins[-1]: #如果這是第一筆push值(x) 或
            self.mins.append(x)                     #self.mins的最上面那個數值>=新進來的push值(x)
                                                    #咱們就把它也append進去self.mins吧！

    def pop(self):
        item=self.main.pop()        
        if item == self.mins[-1]:   #如果item=self.mins的最上面那個數值
            self.mins.pop()         #簡單講就是最新push的值是最小值的話，兩個stack都要一起pop
                                    #這樣才能維持最小值的正確

    def top(self):
        return self.main[-1]        #這個沒問題！直接把self.main的最上面的值return
        
    def getMin(self):
        return self.mins[-1]        #由於每次push時，都有把最小值放進self.mins，所以這邊就輕鬆了#
