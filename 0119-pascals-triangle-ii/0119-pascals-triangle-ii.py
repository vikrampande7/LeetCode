class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1] * c for c in range(1, rowIndex+2)]
        print(triangle)
        for row in range(2, len(triangle)):
            for col in range(1, row):
                triangle[row][col] = triangle[row-1][col] + triangle[row-1][col-1]
        return triangle[rowIndex]