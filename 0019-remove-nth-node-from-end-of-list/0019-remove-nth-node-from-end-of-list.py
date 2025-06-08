# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy = ListNode(0, head)
        # l = dummy
        # r = head 

        # while n > 0 and r:
        #     r = r.next
        #     n -= 1

        # while r:
        #     l = l.next
        #     r = r.next

        # l.next = l.next.next

        # return dummy.next

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        idx = len(nodes)-n
        if idx == 0:
            return head.next

        nodes[idx-1].next = nodes[idx].next

        return head

        