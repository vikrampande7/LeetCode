class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0 for _ in range(size)]
    
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
            self.parent[yset] = self.parent[xset]
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = self.parent[yset]
        else:
            self.parent[xset] = self.parent[yset]
            self.rank[yset] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        # Union All
        for A, B in edges:
            uf.union(A, B)

        noc = set()
        # Count the Distinct Parents
        for i in range(n):
            noc.add(uf.find(i))

        return len(noc)