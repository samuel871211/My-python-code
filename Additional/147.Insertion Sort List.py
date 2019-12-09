# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        else:
            arr = []
            cur = head
            while cur != None:
                arr.append(cur.val)
                cur = cur.next
            print(arr)

            for index in range(1,len(arr)):
                i = index 
                while i > 0:
                    if arr[i] < arr[i-1]:
                        arr[i],arr[i-1] = arr[i-1],arr[i]
                        i -= 1
                    else:
                        break
            newhead = ListNode(arr[0])
            cur = newhead
            for i in range(1,len(arr)):
                cur.next = ListNode(arr[i])
                cur = cur.next
            return newhead
