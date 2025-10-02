class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = [set() for _ in range(9)]
        COLS = [set() for _ in range(9)]
        SUBG = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == ".":
                    continue

                if char in ROWS[i]:
                    return False
                ROWS[i].add(char)

                if char in COLS[j]:
                    return False
                COLS[j].add(char)
                
                SG = (i // 3) * 3 + (j // 3)
                if char in SUBG[SG]:
                    return False
                SUBG[SG].add(char)

        return True