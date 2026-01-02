class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, A):
        if self.parent[A] != A:
            self.parent[A] = self.find(self.parent[A])
        return self.parent[A]

    def union(self, A, B):
        Aset = self.find(A)
        Bset = self.find(B)
        if Aset == Bset:
            return True
        if self.rank[Aset] > self.rank[Bset]:
            self.parent[Bset] = Aset
        elif self.rank[Bset] > self.rank[Aset]:
            self.parent[Aset] = Bset
        else:
            self.parent[Aset] = Bset
            self.rank[Aset] += 1    

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        res = []
        d = defaultdict(list)
        for A, B in pairs:
            uf.union(A, B)
        for i in range(len(s)):
            d[uf.find(i)].append(s[i])
        for k in d.keys():
            d[k].sort(reverse=True)
        for i in range(len(s)):
            res.append(d[uf.find(i)].pop())
        return ''.join(res)

        