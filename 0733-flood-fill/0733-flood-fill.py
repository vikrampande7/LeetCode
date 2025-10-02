class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])

        # Edge case, if the newColor is already oldColor return the image as it is
        oldColor = image[sr][sc]
        if color == oldColor:
            return image

        def dfs(r, c):
            # Current (r, c) (1, 1)
            # Value above (0, 1) -> r-1, c
            # Value below (2, 1) -> r+1, c
            # Value left (1, 0)  -> r, c-1
            # Value right (1, 2) -> r, c+1 

            if image[r][c] == oldColor:
                image[r][c] = color

                # Check the upper and lower, left and right bounds and if inside, then process the pixel
                if r > 0:
                    dfs(r-1, c)
                if r+1 < ROWS:
                    dfs(r+1, c)
                if c > 0:
                    dfs(r, c-1)
                if c+1 < COLS:
                    dfs(r, c+1)


        dfs(sr, sc) # Call DFS on starting indices 
        return image      