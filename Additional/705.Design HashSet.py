class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        

    def add(self, key: int) -> None:
        self.arr.append(key)
        

    def remove(self, key: int) -> None:
        while key in self.arr:
            self.arr.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.arr:
            return True
        return False
