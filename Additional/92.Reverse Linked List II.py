# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        arr = []
        while cur != None:
            arr.append(cur.val)
            cur = cur.next
        arr1 = arr[:m-1]
        arr2 = arr[m-1:n]
        arr2.reverse()
        arr3 = arr[n:]
        arr = arr1+arr2+arr3
        new = ListNode(arr[0])
        temp = new
        for i in range(1,len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return new
