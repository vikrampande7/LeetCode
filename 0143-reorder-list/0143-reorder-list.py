# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reverse the second half of the list
        Merge two lists
        Multiple pointers
        Save broken lists
        Time Complexity O(n)
        Space Complexity O(1)
        """
        
        # Find the second half
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
            
        # Reverse the list from second half
        second = s.next # Starting point of second list
        prev =  None
        s.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # Merge two lists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        