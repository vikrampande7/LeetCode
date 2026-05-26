class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        upper = set()
        lower = set()
        special = 0

        for c in word:
            if c.isupper():
                upper.add(c)
            if c.islower():
                lower.add(c)
        
        for c in lower:
            if c.upper() in upper:
                special += 1
            
        return special
        