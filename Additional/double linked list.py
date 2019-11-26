class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.head == None or index < 0 or index >= self.size:
            return -1
        else:
            count = 0
            cur = self.head
            while count < index:
                cur = cur.next
                count += 1
            return cur.val

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
        else:
            NewHead = Node(val)
            temp = self.head
            self.head = NewHead
            self.head.next = temp
            temp.prev = self.head
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
        else:
            NewTail = Node(val)
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = NewTail
            NewTail.prev = cur
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return -1
        else:
            NewNode = Node(val)
            if index == 0:
                if self.head == None:
                    self.head = NewNode
                else:
                    temp = self.head
                    self.head = NewNode
                    self.head.next = temp
                    temp.prev = self.head
            elif index == self.size:
                count = 1
                cur = self.head
                while count < index:
                    cur = cur.next
                    count += 1
                cur.next = NewNode
                NewNode.prev = cur
            else:           
                count = 0
                cur = self.head
                while count < index:
                    cur = cur.next
                    count += 1
                curp = cur.prev
                curp.next = NewNode
                NewNode.prev = curp
                NewNode.next = cur
                cur.prev = NewNode
        self.size += 1 

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None or index < 0 or index >= self.size:
            return -1
        else:
            if index == 0:
                self.head = self.head.next
            else:
                count = 0
                cur = self.head
                while count < index:
                    cur = cur.next
                    count += 1
                if index == (self.size - 1):
                    cur.prev.next = None
                else:
                    curp = cur.prev
                    curn = cur.next
                    curp.next = curn
                    curn.prev = curp
                    cur = None
        self.size -= 1
    
    def pre(self):
        if self.head == None:
            return None
        else:
            print(self.head.val)
            cur = self.head
            while cur.next != None:
                print(cur.next.val)
                cur = cur.next
