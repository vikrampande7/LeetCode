class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def checkPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (checkPalindrome(s, l, r - 1) or checkPalindrome(s, l + 1, r))
        return True