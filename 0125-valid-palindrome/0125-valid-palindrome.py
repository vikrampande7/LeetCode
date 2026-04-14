class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        o = ""
        for c in s:
            if c.isalnum():
                o += lower(c)
        l = 0
        r = len(o) - 1

        while l < r:
            if o[l] != o[r]:
                return False
            l += 1
            r -= 1
        
        return True
        