# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr = head
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        n = len(vals)
        twinSum = 0
        for i in range(n):
            if i <= (n/2) - 1:
                j = n - 1 - i
                twinSum = max(twinSum, vals[i] + vals[j])
        return twinSum