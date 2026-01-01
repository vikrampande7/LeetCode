class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0 for i in range(size)]

    def find(self, X):
        if self.parent[X] != X:
            self.parent[X] = self.find(self.parent[X])
        return self.parent[X]

    def union(self, X, Y):
        Xset = self.find(X)
        Yset = self.find(Y)
        if Xset == Yset:
            return
        if self.rank[Xset] > self.rank[Yset]:
            self.rank[Yset] = Xset
        elif self.rank[Yset] > self.rank[Xset]:
            self.rank[Xset] = Yset
        else:
            self.rank[Yset] = Xset
            self.rank[Yset] += 1

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        nop = n
        for t, f1, f2 in logs:
            if nop == 1:
                return t
            else:
                uf.union(f1, f2)
                nop -= 1
        return -1
        