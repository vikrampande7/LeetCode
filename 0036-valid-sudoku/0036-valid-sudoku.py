class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        ROWS = [set() for _ in range(n)]
        COLS = [set() for _ in range(n)]
        BOXES = [set() for _ in range(n)]

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
                if val in BOXES[boxIdx]:
                    return False
                BOXES[boxIdx].add(val)
        
        return True