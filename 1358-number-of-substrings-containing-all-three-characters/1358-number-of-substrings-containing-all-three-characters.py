class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # def has_all(freq):
        #     return all(f > 0 for f in freq)
        # l = 0
        # r = 0
        # res = 0
        # freq = [0] * 3
        # while l < len(s):
        #     freq[ord(s[r]) - ord("a")] += 1
        #     while has_all(freq):
        #         res += len(s) - r
        #         freq[ord(s[l]) - ord("a")] -= 1
        #         l += 1
        #     r += 1
        # return res

        last = [-1] * 3
        res = 0
        for p in range(len(s)):
            last[ord(s[p]) - ord("a")] = p
            res += 1 + min(last)
        return res 