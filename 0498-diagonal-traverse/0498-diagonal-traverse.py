class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        mp = defaultdict(list) # defaultdict key-vals are in sorted order, hence reverse EVEN diagonals not odd
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                mp[r+c].append(mat[r][c])

        for i in range(ROWS+COLS-1):
            vals = mp[i]
            if i % 2 == 0: 
                vals.reverse()
                res.extend(vals)
            else:
                res.extend(vals)
        
        return res