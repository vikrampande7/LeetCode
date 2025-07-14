class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstras BFS
        visit = set()
        minHeap = [(0, k)]
        edges = collections.defaultdict(list)
        for e, v, w in times:
            edges[e].append((v, w))
        res = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = max(res, weight)
            for nei, neiWeight in edges[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (weight+neiWeight, nei))
        return res if len(visit) == n else -1