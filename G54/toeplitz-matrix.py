class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        for col in range(cols):
            p1, p2 = rows - 1, col
            number = matrix[p1][p2]
            while p1 >= 0 and p2 >= 0:
                p1 -= 1
                p2 -= 1
                if p1 >= 0 and p2 >= 0 and matrix[p1][p2] != number:
                    return False

        for row in range(1, rows):
            p1, p2 = row, cols - 1
            number = matrix[p1][p2]
            while p1 >= 0 and p2 >= 0:
                p1 -= 1
                p2 -= 1
                if p1 >= 0 and p2 >= 0 and matrix[p1][p2] != number:
                    return False

        return True
