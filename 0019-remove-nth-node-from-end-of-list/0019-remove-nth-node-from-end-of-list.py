# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        - Two pointers with difference of n
        - Increment these two pointers till right pointer becomes Null
        - Add an extra node to account for left pointer to be at previous node of the node that we want to delete
        - Point the left pointer to element at the end after removing nth element from end
        - Time complexity: O(n)
        """
        
        extra = ListNode(0, head)
        left = extra
        right = head
        
        while n>0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return extra.next
        