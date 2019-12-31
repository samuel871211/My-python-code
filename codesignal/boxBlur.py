def boxBlur(image):
    temp ,final = [] , []
    i , j = 0 , 0
    helper(image,temp,final,i,j)
    return final
def helper(image,temp,final,i,j):
    add = 0
    for ver in range(i,i+3):
        for hor in range(j,j+3):
            add += image[ver][hor]
    add = add // 9
    temp.append(add)
    if j+3 < len(image[0]):
        j += 1
        helper(image,temp,final,i,j)
    else:
        final.append(temp)
        temp = []
        if i+3 < len(image):
            i += 1
            j = 0
            helper(image,temp,final,i,j)
