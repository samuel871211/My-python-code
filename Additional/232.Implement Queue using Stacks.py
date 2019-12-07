class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.temp = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.data) != 0:
            for i in range(len(self.data)-1):
                self.temp.append(self.data[-1])
                self.data = self.data[:len(self.data)-1]
            cur = self.data[-1]
            self.data = []
            a = len(self.temp)
            for i in range(a):
                self.data.append(self.temp[-1])
                self.temp = self.temp[:len(self.temp)-1]
            return cur

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.data != 0:
            for i in range(len(self.data)-1):
                self.temp.append(self.data[-1])
                self.data = self.data[:len(self.data)-1]
            cur = self.data[-1]
            a = len(self.temp)
            for i in range(a):
                self.data.append(self.temp[-1])
                self.temp = self.temp[:len(self.temp)-1]
            return cur

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.data) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
