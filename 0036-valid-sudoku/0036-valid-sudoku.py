class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                # Check row
                if num in rows[i]:
                    return False
                rows[i].add(num)
                # Check column
                if num in columns[j]:
                    return False
                columns[j].add(num)
                # Check subgrid
                sg = (i // 3) * 3 + (j // 3)
                if num in subgrids[sg]:
                    return False
                subgrids[sg].add(num)
        return True
        