# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        vals_to_remove = set(nums)
        while head and head.val in vals_to_remove:
            head = head.next
        if not head:
            return None
        curr = head
        while curr.next: ### You missed this, it should be curr.next instead of curr
            if curr.next.val in vals_to_remove:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
