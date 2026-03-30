class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        currStr = "1"
        for _ in range(n-1):
            nxtStr = ""
            i = j = 0
            while j < len(currStr):
                while(j<len(currStr) and currStr[j]==currStr[i]):
                    j += 1
                nxtStr += str(j-i) + currStr[i]
                i = j
            currStr = nxtStr
        return currStr
        