class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)            
        edgeCnt = {}
        leaves = deque()
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                leaves.append(node)
            edgeCnt[node] = len(neighbors)
        while leaves:
            if n <= 2:
                return list(leaves) # Only two nodes and they can be roots because the minimum height will be 2
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in graph[node]:
                    edgeCnt[nei] -= 1
                    if edgeCnt[nei] == 1:
                        leaves.append(nei)