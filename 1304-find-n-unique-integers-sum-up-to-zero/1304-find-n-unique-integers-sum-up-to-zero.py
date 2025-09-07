class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = [0 for _ in range(n)]
        start = 1
        i = 0
        while (i+1 < n):
            arr[i] = start
            arr[i+1] = -start
            i += 2
            start += 1
        return arr