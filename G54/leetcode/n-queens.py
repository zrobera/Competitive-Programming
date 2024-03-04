class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.ans = []
        def isPossible(row,col,board):
            for i in range(n):
                if board[i][col] == "Q":
                    return False
            r,c = row,col
            while r >=0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            r,c = row,col
            while r < n and c < n:
                if board[r][c] == "Q":
                    return False
                r += 1
                c += 1
            r,c = row,col
            while r >=0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            r,c = row,col
            while r < n and c >= 0:
                if board[r][c] == "Q":
                    return False
                r += 1
                c -= 1
            return True

        def backtrack(board,row):
            if row >= n:
                temp = []
                for i in range(n):
                    temp.append("".join(board[i]))
                self.ans.append(temp)
            
            for col in range(n):
                if isPossible(row,col,board):
                    board[row][col] = "Q"
                    backtrack(board,row+1)
                    board[row][col] = "."
        
        board = [["."]*n for i in range(n)]
        backtrack(board,0)
        return self.ans

        
