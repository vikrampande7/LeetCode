# Kruskal's Algorithm
class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.group = [i for i in range(size)]
    
    def find(self, x):
        if self.group[x] != x:
            self.group[x] = self.find(self.group[x])
        return self.group[x]

    def union(self, x, y):
        x_s = self.find(x)
        y_s = self.find(y)
        if x_s == y_s:
            return False
        if self.rank[x_s] > self.rank[y_s]:
            self.group[y_s] = x_s
        elif self.rank[x_s] < self.rank[y_s]:
            self.group[x_s] = y_s
        else:
            self.group[x_s] = y_s
            self.rank[y_s] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for p1 in range(n):
            for p2 in range(p1+1, n):
                weight = abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])
                edges.append((weight, p1, p2))
        edges.sort() # Step 1 of Kruskals Algorithm 
        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0
        for w, p1, p2 in edges:
            if uf.union(p1, p2):
                mst_cost += w
                edges_used += 1
                if edges_used == n - 1:
                    break
        return mst_cost 
