class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        def isValidcandidate(row,col,visited):
            return (0 <= row < self.rows) and (0 <= col < self.cols) and ((row,col) not in visited)
        def backtrack(combinations,row,col,visited,ctr):
            if combinations == word:
                return True
            if len(combinations) >= len(word):
                return
            # if board[row][col] != word[ctr]:
            #     return
            for r,c in [(row, col+1),(row+1,col), (row-1,col), (row,col-1)]:
                if isValidcandidate(r,c,visited) and board[r][c] == word[ctr]:
                    if backtrack(combinations+board[r][c],r,c,visited|set([(r,c)]),ctr+1):
                        return True
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0]:
                    if backtrack(board[i][j],i,j,set([(i,j)]),1):
                        return True
        return False

