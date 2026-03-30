class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (Counter(s1[::2]) == Counter(s2[::2])) and (Counter(s1[1::2]) == Counter(s2[1::2])):
            return True
        else:
            return False