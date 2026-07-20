class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        num_rows, num_cols = len(grid), len(grid[0])
        for _ in range(k):
            new_grid = [[0] * num_cols for _ in range(num_rows)]
            for row in range(num_rows):
                for col in range(num_cols - 1):
                    new_grid[row][col + 1] = grid[row][col]

            for row in range(num_rows - 1):
                new_grid[row + 1][0] = grid[row][num_cols - 1]
                
            new_grid[0][0] = grid[num_rows - 1][num_cols - 1]

            grid = new_grid

        return grid