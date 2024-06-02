class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            MxN Grid -> Backtracking
            Recursive DFS
            No revisiting of Character
            Time Complexity -> O(n*m*4^n)
        """
        
        rows, cols = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r<0 or c<0 or r>= rows or c >= cols or word[i]!= board[r][c] or (r,c) in path):
                return False
            
            path.add((r, c))
            
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): 
                    return True
        
        return False