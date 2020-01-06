import numpy as np

def spiralNumbers(n):
    arr = []
    final = []
    for p in range(n):
        for q in range(n):
            arr.append(0)
        final.append(arr)
        arr = []
    return right(n,1,0,0,final)

def right(n,start,i,j,final):
    while j < len(final[i]) and final[i][j] == 0:
        final[i][j] = start
        start += 1
        j += 1
    # print("right=")
    # print(np.matrix(final))
    if start > n*n:
        return final
    else:
        return down(n,start,i+1,j-1,final)
    
def down(n,start,i,j,final):
    while i < len(final) and final[i][j] == 0:
        final[i][j] = start
        start += 1
        i += 1
    # print("down=")
    # print(np.matrix(final))
    if start > n*n:
        return final
    else:
        return left(n,start,i-1,j-1,final)
    
def left(n,start,i,j,final):
    while j > -1 and final[i][j] == 0:
        final[i][j] = start
        start += 1
        j -= 1
    # print("left=")
    # print(np.matrix(final))
    if start > n*n:
        return final
    else:
        return up(n,start,i-1,j+1,final)
    
def up(n,start,i,j,final):
    while i > -1 and final[i][j] == 0:
        final[i][j] = start
        start += 1
        i -= 1
    # print("up=")
    # print(np.matrix(final))
    if start > n*n:
        return final
    else:
        return right(n,start,i+1,j+1,final)
