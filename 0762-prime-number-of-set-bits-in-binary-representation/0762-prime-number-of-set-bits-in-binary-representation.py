class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        p = 0
        for i in range(left, right+1):
            n = bin(i).count('1')
            if n in primes:
                p += 1
        return p