class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        minLen = min(len(word1), len(word2))
        out = ""
        for i in range(minLen):
            out += word1[i]
            out += word2[i]
        if len(word1) > minLen:
            out += word1[minLen:]
        if len(word2) > minLen:
            out += word2[minLen:]
        return out