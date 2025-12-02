class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        ROWS = [set() for i in range(n)]
        COLS = [set() for i in range(n)]
        BOX =  [set() for i in range(n)]

        for r in range(n):
            for c in range(n):
                val = board[r][c]
                
                if val == ".":
                    continue

                if val in ROWS[r]:
                    return False
                ROWS[r].add(val)

                if val in COLS[c]:
                    return False
                COLS[c].add(val)

                boxIdx = (r // 3) * 3 + c // 3
                if val in BOX[boxIdx]:
                    return False
                BOX[boxIdx].add(val)

        return True
