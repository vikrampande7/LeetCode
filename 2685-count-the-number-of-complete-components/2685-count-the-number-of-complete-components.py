class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for i in range(n)]
        freq = defaultdict(int)
        for v in range(n):
            graph[v] = [v]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        for v in range(n):
            nei = tuple(sorted(graph[v]))
            freq[nei] += 1
        out = 0
        for n, f in freq.items():
            if len(n) == f:
                out += 1
        return out