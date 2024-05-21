class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        - Convert the Number to Binary
        - Count 1s in the number
        """
        n = str(bin(n))
        hamming_weight = 0
        for i in n:
            if i == "1":
                hamming_weight+=1
        return hamming_weight
        