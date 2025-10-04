class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        if len(word1) > len(word2):
            for i in range(len(word2)):
                res += word1[i]
                res += word2[i]
            res += word1[len(word2):]
        elif len(word2) > len(word1):
            for i in range(len(word1)):
                res += word1[i]
                res += word2[i]
            res += word2[len(word1):]
        else:
            for i in range(len(word1)):
                res += word1[i]
                res += word2[i]
        return res
