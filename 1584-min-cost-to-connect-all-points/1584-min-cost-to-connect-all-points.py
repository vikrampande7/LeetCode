class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's Algorithm with BFS, Minheap, and HashSet
        
        # Create an adjucency list for all the nodes and neighbors with cost -> node = [[c1, n1], [c2, n2]]
        N = len(points)

        adj = { i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                mnhttn_dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([mnhttn_dist, j])
                adj[j].append([mnhttn_dist, i])

        # Prim's Algorithm
        finalCost = 0
        minHeap = [[0, 0]]
        visit = set()

        while len(visit) < N: # Run till all points are visited
            cost, p = heapq.heappop(minHeap)
            if p in visit:
                continue
            finalCost += cost
            visit.add(p)

            for neiCost, nei in adj[p]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])

        return finalCost
