# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def compare_lists(headA, headB, l):
            a_curr, b_curr = headA, headB
            for _ in range(l):
                if a_curr == b_curr:
                    return a_curr
                a_curr = a_curr.next
                b_curr = b_curr.next
            return None

        a_len, b_len = 0, 0
        a_curr, b_curr = headA, headB
        
        while a_curr:
            a_len += 1
            a_curr = a_curr.next
        
        while b_curr:
            b_len += 1
            b_curr = b_curr.next


        if a_len > b_len:
            a_curr, b_curr = headA, headB
            for _ in range(a_len-b_len):
                a_curr = a_curr.next
            out = compare_lists(a_curr, b_curr, b_len)
        elif a_len < b_len:
            a_curr, b_curr = headA, headB
            for _ in range(b_len - a_len):
                b_curr = b_curr.next
            out = compare_lists(a_curr, b_curr, a_len)
        else:
            a_curr, b_curr = headA, headB
            out = compare_lists(a_curr, b_curr, b_len)
        
        return out