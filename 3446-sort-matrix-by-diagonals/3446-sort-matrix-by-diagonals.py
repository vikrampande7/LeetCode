class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        mp = defaultdict(list)
        res = [[0] * COLS for _ in range(ROWS)]

        # Traverse and store diagonals
        for r in range(ROWS):
            for c in range(COLS):
                mp[r-c].append(grid[r][c])

        # Sort the Dictionary Array
        for i in mp:
            if i >= 0:
                mp[i].sort(reverse=True)
            else:
                mp[i].sort()       

        # Pop and Rebuild
        for r in range(ROWS):
            for c in range(COLS):
                res[r][c] = mp[r-c].pop(0)

        return res