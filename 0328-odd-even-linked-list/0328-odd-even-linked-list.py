# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        even, odd = [], []
        curr = head
        for i in range(size):
            if i % 2 == 0:
                odd.append(curr.val)
            else:
                even.append(curr.val)
            curr = curr.next
        vals = odd + even
        if not vals:
            return None
        sentinel = ListNode(vals[0])
        curr = sentinel
        for v in vals[1:]:
            curr.next = ListNode(v)
            curr = curr.next
        return sentinel