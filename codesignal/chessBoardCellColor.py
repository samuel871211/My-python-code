def chessBoardCellColor(cell1, cell2):
    c1 , c2 = None , None
    if cell1[0] == "A" or cell1[0] == "C" or cell1[0] == "E" or cell1[0] == "G":
        if int(cell1[1])%2 == 1:
            c1 = 0
        else:
            c1 = 1
    else:
        if int(cell1[1])%2 == 1:
            c1 = 1
        else:
            c1 = 0 
    if cell2[0] == "A" or cell2[0] == "C" or cell2[0] == "E" or cell2[0] == "G":
        if int(cell2[1])%2 == 1:
            c2 = 0
        else:
            c2 = 1
    else:
        if int(cell2[1])%2 == 1:
            c2 = 1
        else:
            c2 = 0
    if c1 == c2:
        return True
    return False
