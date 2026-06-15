# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        mid = len(vals) // 2
        vals.pop(mid)

        dummy = ListNode()
        curr = dummy
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next