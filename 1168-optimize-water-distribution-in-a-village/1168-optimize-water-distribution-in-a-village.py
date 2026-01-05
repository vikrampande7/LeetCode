class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size+1))
        self.rank   = [0] * (size+1)

    def find(self, X):
        if self.parent[X] != X:
            self.parent[X] = self.find(self.parent[X])
        return self.parent[X]

    def union(self, X, Y):
        xs, ys = self.find(X), self.find(Y)
        if xs == ys:
            return False
        if self.rank[xs] > self.rank[ys]:
            self.parent[ys] = xs
        elif self.rank[ys] > self.rank[xs]:
            self.parent[xs] = ys
        else:
            self.parent[xs] = ys
            self.rank[ys] += 1
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        sorted_edges = []
        for i, w in enumerate(wells):
            sorted_edges.append((w, 0, i+1))
        for h1, h2, w in pipes:
            sorted_edges.append((w, h1, h2))
        sorted_edges.sort(key=lambda x: x[0])
        uf = UnionFind(n)
        total_cost = 0
        for cost, h1, h2 in sorted_edges:
            if uf.union(h1, h2):
                total_cost += cost
        return total_cost
        