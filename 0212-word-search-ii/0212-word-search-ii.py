class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

    def insert(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.eow = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.insert(w)

        ROWS, COLS = len(board), len(board[0])

        res, visit = set(), set()

        def dfs(node, row, col, wordSoFar):
            if (row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visit or board[row][col] not in node.children):
                return 

            visit.add((row, col))
            node = node.children[board[row][col]]
            wordSoFar += board[row][col]
            if node.eow:
                res.add(wordSoFar)

            dfs(node, row+1, col, wordSoFar)
            dfs(node, row-1, col, wordSoFar)
            dfs(node, row, col+1, wordSoFar)
            dfs(node, row, col-1, wordSoFar)

            visit.remove((row, col))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c, "")


        return list(res)


        