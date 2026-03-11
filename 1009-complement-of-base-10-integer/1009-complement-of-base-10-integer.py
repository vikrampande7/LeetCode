class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)
        c = "0b"
        print(b)
        for i in range(2, len(b)):
            if b[i] == '0':
                c += '1'
            if b[i] == '1':
                c += '0'
        return int(c, 2)