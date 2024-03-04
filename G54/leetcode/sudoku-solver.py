class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isPossible(r,c,k):
            for i in range(9):             
                if board[i][c]==k:
                    print(board[i][c],k) 
                    return False
                if board[r][i]==k: 
                    return False
                if board[3*(r//3) + i//3][3*(c//3) + i%3]==k: 
                    return False
            return True    

        def backtrack(r,c):
            if r==9:
                return True
            if c==9:
                return backtrack(r+1,0)    
            if board[r][c]=='.':
                for k in range(1,10):
                    if isPossible(r,c,str(k))==True:
                        board[r][c]=str(k)
                        if backtrack(r,c+1):
                            return True
                        board[r][c]='.'
                return False
            return backtrack(r,c+1)        

        backtrack(0,0)

        