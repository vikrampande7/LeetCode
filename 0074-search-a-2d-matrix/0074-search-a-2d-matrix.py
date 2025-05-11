class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        searchSpace = []

        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                searchSpace = matrix[i]
                if len(searchSpace) == 1 and searchSpace[0] == target:
                    return True
                break

        # if not searchSpace:
        #     return False

        start = 0
        end = len(searchSpace) - 1

        while start <= end:
            mid = (start + end) // 2
            if searchSpace[mid] == target:
                return True
            elif target < searchSpace[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return False
            
        