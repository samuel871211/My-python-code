def absoluteValuesSumMinimization(a):
    ans_val = None
    ans_sum = None
    cur = 0
    for i in range(len(a)):
        for j in range(len(a)):
            cur += abs(a[j]-a[i])
        if not ans_sum or cur < ans_sum:
            ans_val = a[i]
            ans_sum = cur
        cur = 0
    return ans_val
