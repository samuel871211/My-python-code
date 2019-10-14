def quicksort(list):
    if len(list) <= 1:
        return list #如果輸入的list長度<=1，就沒有排列的必要了
    else:
        pivot = list[-1] #基準點就設定為list的最後一個數字
        print(pivot) #追蹤每次的基準點
        equal = [] #拿來放跟基準點一樣的數字
        smaller = [] #拿來放比基準點小的數字
        bigger = [] #拿來放比基準點大的數字
        for num in list:
            if num > pivot:
                bigger.append(num) #比基準點大就append進去
            elif num == pivot:
                equal.append(num) #跟基準點一樣就append進去
            else:
                smaller.append(num) #比基準點小就append進去
        print(equal) #追蹤每次的equal
        print(smaller) #追蹤每次的smaller
        print(bigger) #追蹤每次的bigger
    return quicksort(smaller) + equal + quicksort(bigger) #equal就不必再排列了，smaller跟bigger還要再繼續排列，直到len(list)<=1才會return list
    
<test>
list1=[4,3,2,8,7,6,5]
quicksort(list1)

5 #第一個pivot
[5] #第一個equal
[4, 3, 2] #第一個smaller
[8, 7, 6] #第一個bigger
2 #第二個pivot(由於equal已經跑完程序，所以換smaller來繼續跑quicksort)
[2] #第二個equal
[] #第二個smaller
[4, 3] #第二個bigger
3 #如同上述的規律
[3]
[]
[4]
6 #smaller已經跑完程序，換bigger來繼續跑quicksort
[6]
[]
[8, 7]
7 #如同上述的規律
[7]
[]
[8]

[2, 3, 4, 5, 6, 7, 8] #最後結果
