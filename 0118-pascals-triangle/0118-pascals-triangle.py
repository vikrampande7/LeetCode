class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        if numRows >= 1:
            triangle.append([1])
        if numRows >= 2:
            triangle.append([1, 1])
        for r in range(2, numRows):
            prevRow = triangle[r-1]
            newRow = [1]
            for i in range(1, len(prevRow)):
                newRow.append(prevRow[i-1] + prevRow[i])
            newRow.append(1)
            triangle.append(newRow)
        return triangle