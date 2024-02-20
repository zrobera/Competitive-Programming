class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxCol = 0
                for k in range(len(grid)):
                    maxCol = max(grid[k][j], maxCol)
                final = min(maxCol, max(grid[i]))
                ans += final - grid[i][j]
        return ans
        