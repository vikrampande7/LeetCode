class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for i in range(n):
            chars = [0] * 26
            for j in range(i, n):
                ch = ord(s[j]) - ord('a')
                chars[ch] += 1
                if chars[ch] > 2:
                    break
                ans = max(ans, j-i+1)
        return ans