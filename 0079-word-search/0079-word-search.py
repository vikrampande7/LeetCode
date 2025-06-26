class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        seen = set()

        def recursion(r, c, i):
            if i == len(word):
                return True

            if (r<0 or c<0              or
                (r,c) in seen           or
                r >= ROWS or c >= COLS  or
                word[i] != board[r][c]):
                return False     

            seen.add((r, c))
            res = (
                recursion(r+1, c, i+1) or
                recursion(r-1, c, i+1) or
                recursion(r, c+1, i+1) or
                recursion(r, c-1, i+1) )
            seen.remove((r, c))

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if recursion(i, j, 0):
                    return True
        
        return False


        