class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        def helper(pattern, word):
            m, n = len(pattern), len(word)
            for i in range(n-m+1):
                f = True
                for j in range(m):
                    if word[i+j] != pattern[j]:
                        f = False
                        break
                if f:
                    return True
            return False
        res = 0
        for pattern in patterns:
            res += helper(pattern, word)
        return res        