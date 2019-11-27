def matrixElementsSum(matrix):
    cur = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == 0:
                break
            else:
                cur = cur + matrix[j][i]       
    return cur
