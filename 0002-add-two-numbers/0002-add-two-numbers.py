# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        prev = sentinel
        carry = 0
        while l1 or l2 or carry:
            # Get values from each linked list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Find the addition, digit and carry if existst
            addition = val1 + val2 + carry
            digit = addition % 10
            carry = addition // 10

            # Add the new digit to the sentinel Node and update the sentinel pointer
            prev.next = ListNode(digit)
            prev = prev.next

            # Update Lists and got to next if exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return sentinel.next