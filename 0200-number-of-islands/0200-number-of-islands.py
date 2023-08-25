class Solution:
    def foundIsland(self, row: int, col: int,grid: List[List[str]]) -> bool:
        if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])):
            return False
        if grid[row][col] == "0":
            return False
        grid[row][col] = "0"

        for r,c in [(1,0), (0,1), (-1,0), (0,-1)]:
            new_r, new_c = row+r, col+c
            self.foundIsland(new_r, new_c, grid)
        return True



    def numIslands(self, grid: List[List[str]]) -> int:
        r,c = len(grid), len(grid[0])
        count = 0
        for row in range(r):
            for col in range(c):
                if self.foundIsland(row,col,grid):
                    count += 1
        return count