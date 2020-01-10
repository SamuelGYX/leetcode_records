'''
Overview:

    Sort a linked list in O(n log n) time using constant space complexity.

Solution:

    Bottom-up merge sort
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next
        
        dummy = ListNode(0)
        dummy.next = head
        
        step = 1
        while step < length:
            cur, tail = dummy.next, dummy
            while cur:
                a = cur
                b = self.split(cur, step)
                cur = self.split(b, step)
                tail = self.merge(a, b, tail)
            step *= 2
        
        return dummy.next
    
    def split(self, head, n):
        i = 1
        while i < n and head:
            head = head.next
            i += 1
        if not head:
            return None
        res, head.next = head.next, None
        return res
    
    def merge(self, a, b, tail):
        while a and b:
            if a.val < b.val:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        while tail.next:
            tail = tail.next
        return tail