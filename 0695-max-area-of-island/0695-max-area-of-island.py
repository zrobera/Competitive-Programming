class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def islandArea(row,col,grid):
            if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])):
                return 0
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0

            area = 1
            for r,c in [(1,0), (0,1), (-1,0), (0,-1)]:
                new_r, new_c = row+r, col+c
                area += islandArea(new_r, new_c, grid)
            return area

        maxm = float("-inf")
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = islandArea(r,c,grid)
                maxm = max(area,maxm)
        return maxm

        