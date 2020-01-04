def chessKnight(cell):
    pivot = "abcdefgh"
    count = 8
    for i in range(len(pivot)):
        if cell[0] == pivot[i]:
            vertical_4 , vertical_2 = False , False
            if int(cell[1]) == 8 or int(cell[1]) == 1:
                vertical_4 = True
                count -= 4
            elif int(cell[1]) == 7 or int(cell[1]) == 2:
                vertical_2 = True
                count -= 2
            if i == 0 or i == 7:
                if vertical_4:
                    count -= 2
                elif vertical_2:
                    count -= 3
                else:
                    count -= 4
            elif i == 1 or i == 6:
                if vertical_4:
                    count -= 1
                else:
                    count -= 2
            return count
