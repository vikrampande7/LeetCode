class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0 for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        else:
            self.parent[xset] = yset
            self.rank[xset] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for A, B in edges:
            uf.union(A, B)
        noc = set()
        for i in range(n):
            noc.add(uf.find(i))
        return len(noc)