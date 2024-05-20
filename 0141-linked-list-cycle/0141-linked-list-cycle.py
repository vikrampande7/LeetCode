# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        - If Hashmap is used, memory complexity will be O(n)
        - Use Algorithm: Floyds Tortoise and Hare
        - Set up fast and slow pointers
        - Slow increment by 1, fast increment by 2
        - If they meet, then there is a cycle
        - Do this till fast pointer becomes null, if fast becomes null then there is no cycle
        """
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
        