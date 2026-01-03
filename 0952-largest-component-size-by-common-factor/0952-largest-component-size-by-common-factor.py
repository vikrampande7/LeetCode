class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size+1))
        self.rank = [1] * (size+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        ax = self.find(x)
        ay = self.find(y)
        if ax == ay:
            return ax
        if self.rank[ax] > self.rank[ay]:
            ax, ay = ay, ax
            self.parent[ax] = ay
            self.rank[ay] += self.rank[ax]
        return ay

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums))
        for num in nums:
            for factor in range(2, int(sqrt(num))+1):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)

        max_size = 0
        group_count = defaultdict(int)
        for num in nums:
            group_id = uf.find(num)
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])

        return max_size