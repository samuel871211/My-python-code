def sudoku(grid):
    a = set()
    for i in range(1,10):
        a.add(i)  
    return column(grid,a,set())

def column(grid,a,b):
    for i in range(9):
        for j in range(9):
            cur = len(b)
            b.add(grid[i][j])
            if cur == len(b):
                return False
        b = set()
    return row(grid,a,b)

def row(grid,a,b):
    for j in range(9):
        for i in range(9):
            cur = len(b)
            b.add(grid[i][j])
            if cur == len(b):
                return False
        b = set()
    return matrix(grid,a,b,0,0)
     
def matrix(grid,a,b,i,j):
    for hor in range(i,i+3):
        for ver in range(j,j+3):
            cur = len(b)
            b.add(grid[hor][ver])
            if cur == len(b):
                return False
    b = set()
    if j+3 < len(grid[0]):
        return matrix(grid,a,b,i,j+3)
    elif i+3 < len(grid):
        return matrix(grid,a,b,i+3,0)
    else:
        return True
