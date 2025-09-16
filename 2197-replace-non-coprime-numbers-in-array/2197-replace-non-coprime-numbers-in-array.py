class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        def gcd(a, b):
            while b: 
                a, b = b, a % b
            return a

        for num in nums:
            while res and gcd(res[-1], num) > 1:
                prev = res.pop()
                num = (prev * num) // gcd(prev, num)
            res.append(num)

        return res