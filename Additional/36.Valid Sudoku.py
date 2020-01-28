class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = set()
        b = set()
        c = set()
        for row in range(9):
            for col in range(9):
                if board[row][col].isdigit():
                    cur = len(a)
                    a.add(board[row][col])
                    if cur == len(a):
                        return False
                if board[col][row].isdigit():
                    cur = len(b)
                    b.add(board[col][row])
                    if cur == len(b):
                        return False
            a = set()
            b = set()
        return self.helper(0,0,board,c)
        
    def helper(self,i,j,board,c):
        for row in range(i,i+3):
            for col in range(j,j+3):
                if board[row][col].isdigit():
                    cur = len(c)
                    c.add(board[row][col])
                    if cur == len(c):
                        return False
        c = set()
        if j < 6:
            return self.helper(i,j+3,board,c)
        elif i < 6:
            return self.helper(i+3,0,board,c)
        return True
