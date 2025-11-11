"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        stack = [head]
        vals = []
        while stack:
            node = stack.pop()
            vals.append(node.val)
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)

        head = Node(vals[0])
        current = head

        # Create the rest of the list
        for val in vals[1:]:
            new_node = Node(val)
            current.next = new_node
            new_node.prev = current
            current = new_node

        return head