# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        arr = []
        while l1 != None:
            arr.append(l1.val)
            l1 = l1.next
        while l2 != None:
            arr.append(l2.val)
            l2 = l2.next
        arr = sorted(arr)
        newhead = ListNode(arr[0])
        cur = newhead
        for i in range(1,len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return newhead
