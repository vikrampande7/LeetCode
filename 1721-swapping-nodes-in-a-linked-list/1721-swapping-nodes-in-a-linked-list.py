# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_len(head):
            curr = head
            count = 0
            while curr:
                count += 1
                curr = curr.next
            return count
        l = get_len(head)
        
        fn = head
        for i in range(k):
            fn = fn.next

        en = head
        for i in range(l-k):
            en = en.next
        
        fn.val = en.val
        en.val = fn.val

        return head