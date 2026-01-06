class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        paths = []
        stack = [(0, [0])]
        while stack:
            node, path = stack.pop()
            if node == target:
                paths.append(path)
                continue
            for nei in graph[node]:
                stack.append((nei, path + [nei]))
        return paths