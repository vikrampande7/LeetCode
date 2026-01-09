class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        paths = []
        q = deque([(0, [0])])
        while q:
            node, path = q.popleft()
            if node == target:
                paths.append(path)
                continue
            for nei in graph[node]:
                q.append((nei, path + [nei]))
        return paths