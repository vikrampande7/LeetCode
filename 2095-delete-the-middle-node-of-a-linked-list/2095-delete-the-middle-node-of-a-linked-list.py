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
        if head.next == None:
            return None
            
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        mid = n // 2
        curr = head
        for i in range(mid - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head