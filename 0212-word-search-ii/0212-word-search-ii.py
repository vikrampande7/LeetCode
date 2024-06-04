class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        crawler = self
        for w in word:
            if w not in crawler.children:
                crawler.children[w] = TrieNode()
            crawler = crawler.children[w]
        crawler.isWord = True
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        # Add all words in Trie
        for word in words:
            root.addWord(word)
            
        RES, VISITED = set(), set()
        ROWS,COLS = len(board), len(board[0])
        
        
            
        # Write DFS Function
        def dfs(r, c, node, word):
            # Edge Cases
            if ( r < 0 
            or c < 0 
            or r == ROWS 
            or c == COLS 
            or (r,c) in VISITED 
            or board[r][c] not in node.children):
                return 
            
            # Otherwise Mark as visited
            VISITED.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.isWord:
                RES.add(word)
                
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            
            VISITED.remove((r, c))
            
            
        for R in range(ROWS):
            for C in range(COLS):
                dfs(R, C, root, "")
                
        
        return list(RES)
            
            
        
        