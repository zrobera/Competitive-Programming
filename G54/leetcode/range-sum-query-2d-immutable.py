class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = matrix
        for row in range(len(self.prefix_sum)):
            for col in range(1,len(self.prefix_sum[0])):
                self.prefix_sum[row][col] += self.prefix_sum[row][col-1]
        for col in range(len(self.prefix_sum[0])):
            for row in range(1,len(self.prefix_sum)):
                self.prefix_sum[row][col] += self.prefix_sum[row-1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1 == 0 and row1 == 0:
            return self.prefix_sum[row2][col2]
        elif row1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row2][col1-1]
        elif col1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row1-1][col2]
        
        return self.prefix_sum[row2][col2] - self.prefix_sum[row1-1][col2] - self.prefix_sum[row2][col1-1] + self.prefix_sum[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)