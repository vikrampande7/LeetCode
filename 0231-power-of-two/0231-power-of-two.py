class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        out = n & (n-1)
        if out == 0:
            return True
        else:
            return False