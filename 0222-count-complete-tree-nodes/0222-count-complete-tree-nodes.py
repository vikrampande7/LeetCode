# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        Q = deque([root])
        nodeCount = 0
        while Q:
            for _ in range(len(Q)):
                node = Q.popleft()
                nodeCount += 1
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return nodeCount