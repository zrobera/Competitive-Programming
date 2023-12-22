class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rows[i]:
                        return False
                    rows[i].add(board[i][j])

                    curr_box = (i//3,j//3)
                    if board[i][j] in box[curr_box]:
                        return False
                    box[curr_box].add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in cols[i]:
                        return False
                    cols[i].add(board[j][i])
                                
        return True

        