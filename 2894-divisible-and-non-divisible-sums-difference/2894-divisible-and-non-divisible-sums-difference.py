class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nd = [i for i in range(1,n+1) if i % m != 0]
        yd = [i for i in range(1,n+1) if i % m == 0]
        return sum(nd) - sum(yd)