class Node:
    def __init__(self,val):
        self.val = val
        self.next = None #先定義節點，節點內含value(val)跟pointer(next)指向下一個節點

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None #先創造一個空間給頭節點
        self.size = 0 #紀錄整個linked list的長度

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head == None or index<0 or index>=self.size:
            return -1 #以上三種情況無法取值
        else:
            count = 0 #計數用
            cur = self.head
            while index != count: #while statement true，執行25、26行，不然的話就跳出迴圈
                cur = cur.next
                count+=1 #因為linked list要取值的話就只能從head開始數，這個迴圈就是說當數到第index位的時候，return那個節點的value
            return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newHead = Node(val) #創建一個新的頭節點(newHead)
        if self.head == None:
            self.head = newHead #如果原本的頭節點=None，新的頭節點就直接變成頭節點
        else:
            newHead.next = self.head 
            self.head = newHead #把newHead的next連結到self.head，再把newHead定義成self.head
        self.size+=1 #離開迴圈了，不管什麼情況，加一個值到頭都會使整個linked list長度+1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newTail = Node(val) #創建一個新的尾節點(newTail)
        if self.head == None:
            self.head = newTail #如果原本的頭節點=None，新的尾節點就直接變成頭節點
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newTail #因為linked list只能從head開始數，這個迴圈就是說當數到尾節點時(尾節點的next=None)，把newTail加進去
        self.size+=1 #離開迴圈了，不管什麼情況，加一個值到尾都會使整個linked list長度+1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0: #這邊完全就是跟addAtHead一樣的概念
            newHead = Node(val)
            if self.head == None:
                self.head = newHead
            else:
                newHead.next = self.head
                self.head = newHead
        elif index == self.size: #這邊完全就是跟addAtTail一樣的概念
            newTail = Node(val)
            if self.head == None:
                self.head = newTail
            else:
                cur = self.head
                while cur.next != None:
                    cur = cur.next
                cur.next = newTail
        elif index > self.size: #如題目所述，If index is greater than the length, the node will not be inserted.
            return -1
        else: 
            newNode=Node(val) #創建一個新的節點(newNode)
            count = 0 #計數
            cur = self.head
            while index != count:
                prev = cur
                cur = cur.next
                count+=1 #這個迴圈就是把第index個節點設定為cur，前一個節點設定為prev，把newNode插到中間(prev->newNode->cur)
            prev.next = newNode #prev要連上newNode
            newNode.next = cur #newNode要連上cur
        self.size+=1 #離開迴圈了，不管什麼情況，加一個值到指定位置都會使整個linked list長度+1            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head == None or index < 0 or index >=self.size:
            return -1 #跟get的第一個判斷式有點像，以上三種情況無法刪除節點
        elif index == 0:
            self.head = self.head.next
            self.head == None #如果要刪除頭節點的話 @@@@@@@@@@@@@@@@
        else:
            count = 0
            cur=self.head
            while index != count:
                prev = cur
                cur = cur.next
                count+=1 #這個迴圈就是把第index個節點設定為cur，前一個節點設定為prev
            prev.next = cur.next #把prev連結到cur.next(prev->cur.next)
            cur.val= None #把cur刪除
        self.size-=1 #離開迴圈了，不管什麼情況，刪除一個指定位置的節點都會使整個linked list長度-1
