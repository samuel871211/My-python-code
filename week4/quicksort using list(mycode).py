def quicksort(list):
    if len(list) <= 1:
        return list #如果輸入的list長度<=1，就沒有排列的必要了
    else:
        pivot = list[-1] #基準點就設定為list的最後一個數字
        bigger = [] #拿來放比基準點大的數字
        equal = [] #拿來放跟基準點一樣的數字
        smaller = [] #拿來放比基準點小的數字
        for num in list:
            if num > pivot:
                bigger.append(num) #比基準點大就append進去
            elif num == pivot:
                equal.append(num) #跟基準點一樣就append進去
            else:
                smaller.append(num) #比基準點小就append進去
    return quicksort(smaller) + equal + quicksort(bigger) #equal就不必再排列了，smaller跟bigger還要再繼續排列，直到len(list)<=1才會return list
