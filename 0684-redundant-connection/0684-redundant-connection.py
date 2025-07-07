class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        e = len(edges)
        adjm = [[] for i in range(e+1)]

        def dfs(node, par):
            if visit[node]:
                return True

            visit[node] = True
            for nei in adjm[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for u, v in edges:
            adjm[u].append(v)
            adjm[v].append(u)
            visit = [False] * (n+1)

            if dfs(u, -1):
                return [u, v]

        return []
        