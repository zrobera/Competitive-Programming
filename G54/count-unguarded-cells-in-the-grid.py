class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0]*n for i in range(m)]

        for i,j in walls:
            matrix[i][j] = -1

        for i,j in guards:
            matrix[i][j] = 2

        guarded = 0
        for row,col in guards:
            j = col
            i = row-1
            while i >= 0 and matrix[i][j] != -1 and matrix[i][j] != 2:
                if matrix[i][j] != 1:
                    matrix[i][j] = 1
                    guarded += 1
                i-= 1
            i = row+1
            while i < m and matrix[i][j] != -1 and matrix[i][j] != 2:
                if matrix[i][j] != 1:
                    matrix[i][j] = 1
                    guarded += 1
                i += 1
            i = row
            j = col-1
            while j >= 0 and matrix[i][j] != -1 and matrix[i][j] != 2:
                if matrix[i][j] != 1:
                    matrix[i][j] = 1
                    guarded += 1
                j -= 1

            j = col+1
            while j < n and matrix[i][j] != -1 and matrix[i][j] != 2:
                if matrix[i][j] != 1:
                    matrix[i][j] = 1
                    guarded += 1
                j += 1

        return m*n - (guarded+len(guards)+len(walls))



        