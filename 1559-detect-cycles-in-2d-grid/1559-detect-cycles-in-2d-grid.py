class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n,m = len(grid), len(grid[0])
        color = [[0] * m for _ in range(n)]
        def hasCycle(grid: List[List[str]], row: int, col: int, lastCell: Tuple):
            if color[row][col] == 1:
                return True
            if color[row][col] == 2:
                return False
            color[row][col] = 1

            for r,c in [(1,0),(0,1), (-1,0), (0,-1)]:
                new_r, new_c = row + r, col + c
                if (
                    0 <= new_r < n
                    and 0 <= new_c < m
                    and grid[new_r][new_c] == grid[row][col]
                    and (new_r, new_c) != lastCell
                ):
                    if hasCycle(grid,new_r,new_c, (row,col)):
                        return True
            color[row][col] = 2
            return False
        for r in range(n):
            for c in range(m):
                if color[r][c] == 0:
                    if hasCycle(grid,r,c,(-1,-1)):
                        return True
        return False
