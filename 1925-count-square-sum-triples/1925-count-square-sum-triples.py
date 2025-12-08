class Solution:
    def countTriples(self, n: int) -> int:
        squares_map = {}
        tripletCount = 0
        for i in range(1, n+1):
            squares_map[i] = i ** 2
        
        for i in range(1, n+1):
            for j in range(1, n + 1):
                if i ** 2 + j ** 2 in squares_map.values():
                    tripletCount += 1
        
        return tripletCount