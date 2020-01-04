def bishopAndPawn(bishop,pawn):
    pivot = 'abcdefgh'
    temp = []
    for i in range(len(pivot)):
        if bishop[0] == pivot[i]:
            temp.append(i)
        if pawn[0] == pivot[i]:
            temp.append(i)
        if len(temp) == 2:
            break
    if abs(temp[1]-temp[0]) == abs(int(bishop[1])-int(pawn[1])):
        return True
    return False
