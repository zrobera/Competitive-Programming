from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxm = -1
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                total = (sum(grid[row][col:col+3]) + 
                        grid[row+1][col+1] + 
                        sum(grid[row+2][col:col+3])
                    )
                maxm = max(maxm,total)
        return maxm
