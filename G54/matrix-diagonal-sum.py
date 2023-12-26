class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        row,col = 0,0
        while row < len(mat) and col < len(mat[0]):
            total += mat[row][col]
            row += 1
            col += 1
        i,j = 0, len(mat[0])-1

        while i < len(mat) and col >=0:
            total += mat[i][j]
            i += 1
            j -= 1
        if len(mat)%2:
            total -= mat[len(mat)//2][len(mat)//2]
        return total

        