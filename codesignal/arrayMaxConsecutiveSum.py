def arrayMaxConsecutiveSum(a,k):
    ans = 0
    for i in range(k): 
        ans += a[i]
    
    temp = ans
    for i in range(k,len(a)):
        temp = temp - a[i-k] + a[i]
        if temp > ans:
            ans = temp
    return ans
