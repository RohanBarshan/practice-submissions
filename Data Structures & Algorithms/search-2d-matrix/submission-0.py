class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows =  len(matrix)
        cols = len(matrix[0])

        L, R = 0, rows * cols - 1

        while L <= R:
            mid = (L + R) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if target > value:
                L = mid + 1
            elif target < value:
                R = mid - 1
            else:
                return True
        return False