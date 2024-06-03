class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    
    def char_to_idx(self, c):
        return ord(c) - ord('a')
    
    
    # Get the index of character, create a new node for character if not exists, shift pointer to children, update flag once for loop is complete
    def insert(self, word: str) -> None:
        crawler = self.root
        
        for ch in word:
            idx = self.char_to_idx(ch)
            if not crawler.children[idx]:
                crawler.children[idx] = TrieNode()
            crawler = crawler.children[idx]    
            
        crawler.isEnd = True
        

    def search(self, word: str) -> bool:
        crawler = self.root
        
        for c in word:
            idx = self.char_to_idx(c)
            if not crawler.children[idx]:
                return False
            crawler = crawler.children[idx]
            
        return crawler is not None and crawler.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        crawler = self.root
        
        for ch in prefix:
            idx = self.char_to_idx(ch)
            if not crawler.children[idx]:
                return False
            crawler = crawler.children[idx]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)