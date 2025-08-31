class Solution:
    def isValid(self, board, row, col, digit):
        for i in range(9):
            if board[row][i] == digit:
                return False
            if board[i][col] == digit:
                return False

        sr = (row // 3) * 3
        sc = (col // 3) * 3
        for i in range(sr, sr + 3):
            for j in range(sc, sc + 3):
                if board[i][j] == digit:
                    return False
        return True

    def helper(self, board, row, col):
        if row == 9:
            return True
        nrow, ncol = row, col + 1
        if ncol == 9:
            nrow, ncol = row + 1, 0

        if board[row][col] != '.':
            return self.helper(board, nrow, ncol)

        for digit in map(str, range(1, 10)):
            if self.isValid(board, row, col, digit):
                board[row][col] = digit
                if self.helper(board, nrow, ncol):
                    return True
                board[row][col] = '.'

        return False

    def solveSudoku(self, board):
        self.helper(board, 0, 0)

# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         # Recursive calls
#         digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#         def solve(board):
#             for r in range(9):
#                 for c in range(9):
#                     if board[r][c] == '.':
#                         for d in digits:
#                             if isValidDigit(board, r, c, d):
#                                 board[r][c] = d # If valid function is true then set digit
#                                 if solve(board):    
#                                     return True
#                                 board[r][c] = '.' # Explore and if not true then set back to .
#                         return False
#             return True
        
#         # Check validity
#         def isValidDigit(board, r, c, d):
#             for i in range(9):  
#                 if board[i][c] == d or board[r][i] == d:
#                     return False
#             sbg_start = (r // 3) * 3
#             sbg_end = (c // 3) * 3
#             for a in range(3):
#                 for b in range(3):
#                     if board[sbg_start+a][sbg_end+b] == d:
#                         return False
#             return True
        
#         # Call the function
#         solve(board)