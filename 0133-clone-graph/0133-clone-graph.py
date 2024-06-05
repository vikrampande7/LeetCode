"""
    hashMap + DFS + Recursion
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        recordMap = {}
        
        def dfs(node):
            if node in recordMap:
                return recordMap[node]
            
            copied_val = Node(node.val)
            recordMap[node] = copied_val
            
            for n in node.neighbors:
                copied_val.neighbors.append(dfs(n))
                
            return copied_val
        
        if node:
            return dfs(node)
        else:
            return None
        
        
        