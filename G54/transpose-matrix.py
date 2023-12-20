class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0]*len(matrix) for i in range(len(matrix[0]))]

        for i in range(len(matrix[0])):
            k = 0
            for j in range(len(matrix)):
                ans[i][j] = matrix[k][i]
                k += 1
        return ans
        