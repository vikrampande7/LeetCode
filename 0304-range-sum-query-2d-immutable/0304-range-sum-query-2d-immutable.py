class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.prefixSum = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for row in range(len(matrix)):
            self.prefixSum[row][0] = matrix[row][0]
            for col in range(1, len(matrix[0])):
                self.prefixSum[row][col] = self.prefixSum[row][col - 1] + matrix[row][col]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                res += self.prefixSum[row][col2] - self.prefixSum[row][col1 - 1]
            else:
                res += self.prefixSum[row][col2]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)