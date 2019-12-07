class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.temp = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        a = len(self.data)
        if a != 0:
            for i in range(a-1):
                self.temp.append(self.data[0])
                self.data = self.data[1:]
            cur = self.data[0]
            self.data = []
            for i in range(a-1):
                self.data.append(self.temp[0])
                self.temp = self.temp[1:]
            return cur    

    def top(self) -> int:
        """
        Get the top element.
        """
        a = len(self.data)
        if a != 0:
            for i in range(a-1):
                self.temp.append(self.data[0])
                self.data = self.data[1:]
            cur = self.data[0]
            self.temp.append(self.data[0])
            self.data = []
            for i in range(a):
                self.data.append(self.temp[0])
                self.temp = self.temp[1:]
            return cur 

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.data) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
