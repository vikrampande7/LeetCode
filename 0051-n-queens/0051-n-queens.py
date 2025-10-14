class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for _ in range(n)]        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or c in posDiag or c in negDiag:
                    continue
                col.add(c)
                posDiag.add(c)
                negDiag.add(c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(c)
                negDiag.remove(c)
        backtrack(0)
        return res