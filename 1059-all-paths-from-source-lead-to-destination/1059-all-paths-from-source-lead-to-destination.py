class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
        visited = set()
        gray, black = 1, 2
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei == node or nei in visited or not dfs(nei):
                    return False
            visited.discard(node)
            return len(graph[node]) != 0 or node == destination
        return dfs(source) 