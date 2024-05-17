class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        - Setup a substring equal to length of needle
        - Check if that substring exists in haystack
        - if yes return its index
        '''
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
