class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rs, cs = [], []

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rs.append(r)
                    cs.append(c)

        for c in range(COLS):
            for r in rs:
                matrix[r][c] = 0

        for r in range(ROWS):
            for c in cs:
                matrix[r][c] = 0
        