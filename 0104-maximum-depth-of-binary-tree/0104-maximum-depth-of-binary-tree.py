# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ### DFS RECURSIVE
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        ### DFS with Stack - Iterative - PreOrder
        if not root:
            return 0
        stack = [[root, 1]]
        res = 1
        while stack:
            currNode, depth = stack.pop()
            res = max(res, depth)
            if currNode.left:
                stack.append([currNode.left, depth+1])
            if currNode.right:
                stack.append([currNode.right, depth+1])
        return res

        ### BFS with Queue - Iterative
        # if not root:
        #     return 0
        # q = deque([root])
        # level = 0
        # while q:
        #     for i in range(len(q)):
        #         currNode = q.popleft()
        #         if currNode.left:
        #             q.append(currNode.left)
        #         if currNode.right:
        #             q.append(currNode.right)
        #     level += 1
        # return level
        