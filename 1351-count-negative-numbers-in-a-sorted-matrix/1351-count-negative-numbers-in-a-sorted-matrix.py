class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        row_num = len(grid)
        col_num = len(grid[0])
        n_row = -1
        nxt_h = col_num -1
        for row in grid:
            n_row += 1
            start_row = -1
            if row[0] < 0:
                start_row = n_row
                break
            low, high = 0, nxt_h
            start_col = -1
            while low <= high:
                mid = low + (high-low)//2
                if row[mid] < 0:
                    start_col = mid if start_col == -1 or start_col > mid else start_col
                    high = mid-1
                else:
                    low = mid + 1
            nxt_h = start_col if start_col > -1  else col_num-1   
            if start_col > -1:
                ans += col_num - start_col
        num_negative_rows = (row_num - start_row) * col_num if start_row > -1 else 0
        ans += num_negative_rows
        return ans
