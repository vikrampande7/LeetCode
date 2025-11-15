"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None} #to handle .next null case
        curr = head
        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy_node = hashmap[curr]
            copy_node.next = hashmap[curr.next]
            copy_node.random = hashmap[curr.random]
            curr = curr.next
        return hashmap[head]