class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = sorted(str(n))
        s = "".join(s)

        multiples = []
        for i in range(30):
            num = 2 ** i
            num = sorted(str(num))
            numS = "".join(num)
            multiples.append(numS) 

        if s in multiples:
            return True
        else:
            return False