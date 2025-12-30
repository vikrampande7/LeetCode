class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]  

    def union(self, x, y):
        xset = self.find(x) # Get the parents
        yset = self.find(y)
        # Check the height of the tree, and assign the parent that has maximum height
        if self.rank[xset] < self.rank[yset]: 
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        noc = n
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    noc -= 1
                    uf.union(i, j)
        return noc
        