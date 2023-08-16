class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(row,col):
            image[row][col] = color
            for i,j in ((row-1,col), (row+1,col), (row, col-1), (row,col+1)):
                if 0 <= i < m and 0 <= j < n and image[i][j] == start:
                    dfs(i,j)
        start, m, n = image[sr][sc], len(image), len(image[0])
        if start != color:
            dfs(sr,sc)
        return image