# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Compare the elements of two LLs and append whichever is greater
        If L1 != L2, append all the remaining elements is the list whichever is not empty
        """
        dummy = node = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
                
            node = node.next
            
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
                
                
        return dummy.next
            
        