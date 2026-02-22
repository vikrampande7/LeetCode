class Solution:
    def binaryGap(self, n: int) -> int:
        maxGap = 0
        s = str(bin(n))
        print(s)
        ones_idx = []
        for i in range(len(s)):
            if s[i] == "1":
                ones_idx.append(i)
        if len(ones_idx) <= 1:
            return 0
        maxGap = 0
        for i in range(len(ones_idx) - 1):
            currGap = ones_idx[i+1] - ones_idx[i]
            maxGap = max(maxGap, currGap)
        return maxGap