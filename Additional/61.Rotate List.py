# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None or k == 0: return head
        count = 1
        tail = head
        while tail.next:
            count += 1
            tail = tail.next
        if count == k: 
            return head
        if count < k: 
            k = k % count
        count = count - k
        for i in range(count):
            temp = head
            while temp.next:
                temp.val , temp.next.val = temp.next.val , temp.val
                temp = temp.next
        return head 
