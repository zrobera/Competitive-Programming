class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n= len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        queue = deque([(0,0,1)])
        visited = set([(0,0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while queue:
            r, c , dist = queue.popleft()
            if r == n-1 and c == n-1:
                return dist
            for i,j in directions:
                nr , nc = r+i, c+j
                if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc] and (nr,nc) not in visited:
                    queue.append((nr,nc, dist+1))
                    visited.add((nr,nc))
        return -1
        