#10/27更新第二版程式碼的註解#

def smaller(list): #定義一個函式為smaller
    pivot = list[-1] #基準點設定為list的最後一個數字
    small = [] #創造一個list空間等等要放比pivot小的數字進來
    for num in list: #把list裡面的每個數字都抓出來
        if num < pivot: #然後跟pivot比較，如果比pivot小的話
            small.append(num) #就把它append進small這個list
        else: #要不然
            continue #就跳下一個迴圈執行
    return small #最後回傳small這個list
def bigger(list):
    pivot = list[-1]
    big = []
    for num in list:
        if num > pivot:
            big.append(num)
        else:
            continue
    return big
def equal(list):
    pivot = list[-1]
    equ = []
    for num in list:
        if num == pivot:
            equ.append(num)
        else:
            continue
    return equ
def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        left = smaller(list) #呼叫smaller函式，並且把其回傳的值丟到left裡面，以便等等進行運算
        mid = equal(list)
        right = bigger(list)
    return quicksort(left) + mid + quicksort(right) #最後按照順序回傳quicksort過後的left、mid(這個不用再quicksort)、right
