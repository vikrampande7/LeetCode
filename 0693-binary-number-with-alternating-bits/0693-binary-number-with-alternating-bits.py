class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        return all(b[i] != b[i+1] for i in range(2, len(b)-1))
               