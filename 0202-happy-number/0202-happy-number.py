class Solution:
    def isHappy(self, n: int) -> bool:

        def findHappy(num):
            out = 0
            while num:
                digit = num % 10
                digitSquared = digit ** 2
                out += digitSquared
                num = num // 10
            return out

        visit = set()
        while n not in visit:
            visit.add(n)
            n = findHappy(n)

            if n == 1:
                return True

        return False