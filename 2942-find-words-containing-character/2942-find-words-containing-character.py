class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        idx = []
        for i in range(0, len(words)):
            if x in words[i]: idx.append(i)
        return idx

        