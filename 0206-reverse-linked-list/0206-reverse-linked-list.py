# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            nextVal = curr.next     # get the next value nextVal
            curr.next = prev        # point curr next pointer to to prev
            prev = curr             # update prev to curr
            curr = nextVal     # point curr to nextVal
        return prev