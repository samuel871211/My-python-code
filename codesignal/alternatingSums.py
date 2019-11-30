def alternatingSums(a):
    b = 0
    c = 0
    d = []
    for i in range(0,len(a),2):
        b = b + a[i]
    for j in range(1,len(a),2):
        c = c + a[j]
    d.append(b)
    d.append(c)
    return d
