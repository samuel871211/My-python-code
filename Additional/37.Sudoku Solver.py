class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        for col in range(9):
            for row in range(9):
                if board[col][row] == ".":
                    for i in range(1,10):
                        board[col][row] = str(i)
                        if self.vaild(board,col,row) == True:
                            if self.solveSudoku(board) == True:
                                return True
                    board[col][row] = "."
                    return False
        return True

    def vaild(self,board,col,row):
        for i in range(9):
            if row != i and board[col][row] == board[col][i]:
                return False
            if col != i and board[col][row] == board[i][row]:
                return False
        
        for i in range(3*(col//3),3*(col//3)+3):
            for j in range(3*(row//3),3*(row//3)+3):
                if i != col and j != row and board[col][row] == board[i][j]:
                    return False       
        return True
