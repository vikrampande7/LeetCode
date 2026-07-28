class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = len(s) // 2
        base = sorted(s[:p])
        m = [s[p]] if len(s) % 2 == 1 else []
        r_base = base[::-1]
        return "".join(base+m+r_base)