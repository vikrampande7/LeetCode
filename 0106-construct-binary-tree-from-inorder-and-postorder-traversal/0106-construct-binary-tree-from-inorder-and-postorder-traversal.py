# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postIdx = len(postorder) - 1
        self.inIdx = len(postorder) - 1
        def dfs(limit):
            if self.postIdx < 0:
                return None
            if inorder[self.inIdx] == limit:
                self.inIdx -= 1
                return None
            root = TreeNode(postorder[self.postIdx])
            self.postIdx -= 1
            root.right = dfs(root.val)
            root.left = dfs(limit)
            return root
        return dfs(float("inf"))