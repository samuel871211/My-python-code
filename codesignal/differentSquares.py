def differentSquares(a):
    if len(a) < 2 or len(a[0]) < 2:
        return 0
    else:
        return helper(a,[],0,0)
        
def helper(a,final,i,j):
    temp = ""
    for p in range(i,i+2):
        for q in range(j,j+2):
            temp += str(a[q][p])
    final.append(int(temp))
    if i < len(a[0])-2:
        return helper(a,final,i+1,j)
    elif j < len(a)-2:
        return helper(a,final,0,j+1)
    else:
        if len(final) == 1:
            return 1
        final = sorted(final)
        count = 1
        for i in range(len(final)-1):
            if final[i] != final[i+1]:
                count += 1
        return count 
