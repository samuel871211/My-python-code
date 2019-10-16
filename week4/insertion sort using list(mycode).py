def insertion_sort(list):
    for index in range(1,len(list)): #最左邊的數字沒得比較，所以從第1個數字開始比
        value = list[index] #把第index位的數字取出來等等需要來比較
        i = index - 1 #要跟左邊的那個數字來比較
        while i >= 0: #一直跟左邊的比，直到到最左邊的數字
            if value < list[i]: #右邊比左邊小
                list[i+1] = list[i] #把左邊的位置丟到右邊
                list[i] = value #把左邊的值丟到右邊
                i = i - 1 #一直跟左邊的比，直到到最左邊的數字
            else:
                break #This is an In-place version because this function doesn't create any extra lists to place the sorted numbers. 
          
