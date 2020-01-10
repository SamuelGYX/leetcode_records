'''
Overview:
    
    Sort a linked list using insertion sort.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # dummy: new preHead
        dummy, cur = ListNode(0), head
        prev = dummy
        while cur:
            nxt = cur.next
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            # insert cur after pre
            cur.next, prev.next = prev.next, cur
            # initialize prev back to preHead; update cur
            prev, cur = dummy, nxt
        return dummy.next