"""
Recursion when string contains DOT
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        crawler = self.root
        for c in word:
            if c not in crawler.children:
                crawler.children[c] = TrieNode()
            crawler = crawler.children[c]
        crawler.word = True

    def search(self, word: str) -> bool:
        def dfs(idx, root):
            crawler = root
            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for child in crawler.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in crawler.children:
                        return False
                    crawler = crawler.children[c]
            return crawler.word
        
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)