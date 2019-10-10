# 自我介紹
姓名：陳昱昇

這是資料結構與演算法的Python自學歷程~裡面會記錄我每個禮拜的進度

還會根據我的理解，來做一些筆記，當然這不可能完全正確，有錯誤歡迎指證！

# week2 linked list
是由node(節點)與pointer(指向)所組成

node(節點)可以想成箱子(就是在記憶體所佔的位置)

pointer(指向)就是箱子跟箱子之間的箭頭指向

linked list的好處就是在記憶體中不需要一個連續的空間來儲存，可以利用零散的位置來儲存資料

然而array卻相反，但是array在尋找資料的時候會比較簡單，而且array在搬運的時候會很麻煩，因為要整組一起

以下圖片和文字講解的來源取自http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html

![image](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/LinkedList/Intro/f2.png?raw=true)

Node1：

以int的data，記錄正整數7。

本身的記憶體位置為0x1001042f0。

以「node之pointer」，記錄(指向)下一個node之記憶體位置(0x100104300)。

Node2：

以int的data，記錄正整數3。

本身的記憶體位置為0x100104300。

由於在Node1中的「node之pointer」指向了Node2之記憶體位置，因此，便能夠經由Node1「找到」Node2。

以「node之pointer」，記錄(指向)下一個node之記憶體位置(0x100104310)。

Node3：

以int的data，記錄正整數14。

本身的記憶體位置為0x100104310。

由於在Node2中的「node之pointer」指向了Node3之記憶體位置，因此，便能夠經由Node2「找到」Node3。

以「node之pointer」，記錄(指向)NULL，表示Linked list的最後一個node。

# week3 stack queue
stack就像疊盤子一樣，從下面疊到上面，抽取的時候也是從上面開始抽

stack必須要有的功能：

push：把資料放進stack裡面

pop：把最上面的資料從stack中移除

top：回傳最上面的那筆資料

IsEmpty：確認stack裡面是否有資料

getSize：回傳stack裡面的資料個數

queue就像排隊一樣，從前面開始排，然後不能插隊

push必須有的功能：

push：把資料從queue的後面放進去

pop：把front所指向的資料從queue中移除

getFront：回傳front所指向的資料

getBack：同理，回傳back所指向的資料

IsEmpty：確認queue裡面是否有資料

getSize：回傳queue裡面的資料個數
