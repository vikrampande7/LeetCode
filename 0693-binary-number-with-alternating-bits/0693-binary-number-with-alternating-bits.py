class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        print(b[2:])    
        for i in range(2, len(b)-1):
            if b[i] != b[0]:
                continue
            else:
                return False
        return True       