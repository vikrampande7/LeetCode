# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return 

        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        prev, root = None, head
        for i in range(l // 2):
            prev = root
            root = root.next

        if prev:
            prev.next = None

        node = TreeNode(root.val)
        node.left = self.sortedListToBST(head if prev else None)
        node.right = self.sortedListToBST(root.next)

        return node