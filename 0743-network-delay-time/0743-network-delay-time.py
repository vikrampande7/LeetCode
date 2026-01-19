class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijktra's Algorithm
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        visited = set()
        heap = [(0, k)] # Distance to itself
        t = 0
        while heap:
            w, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t, w)
            for nei, wei in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (w+wei, nei))
        return t if len(visited) == n else -1
