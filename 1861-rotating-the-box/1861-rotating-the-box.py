class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(boxGrid), len(boxGrid[0])
        res = [["." for k in range(m)] for _ in range(n)]
        for i in range(m):
            lowest = n - 1
            for j in range(n-1, -1, -1):
                if boxGrid[i][j] == "#":
                    res[lowest][m-i-1] = "#"
                    lowest -= 1
                if boxGrid[i][j] == "*":
                    res[j][m-i-1] = "*"
                    lowest = j - 1
        return res