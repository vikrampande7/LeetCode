# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ### HashSet
        # seen = set()
        # curr = head
        # while curr:
        #     if curr in seen:
        #         return True
        #     seen.add(curr)
        #     curr = curr.next
        # return False

        ### Floyds Tortoise and Hare Algorithm
        f, s = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False