class ListNode:
    
    def __init__(self,val):
        self.val = val
        self.next = None

class MyHashSet:
    
    def __init__(self,capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity   
        
    def add(self,key):
        a = MD5.new()
        a.update(key.encode("utf-8"))
        val = int(a.hexdigest(),16)
        rem = val % self.capacity
        
        if self.data[rem] == None:
            self.data[rem] = ListNode(val)
        else:
            det = True
            if self.data[rem].val == val:
                det = False
            if det:              
                temp = self.data[rem]
                while temp.next != None and temp.next.val != val:
                    temp = temp.next
                if temp.next == None:
                    temp.next = ListNode(val)
    
    def remove(self,key):
        a = MD5.new()
        a.update(key.encode("utf-8"))
        val = int(a.hexdigest(),16)
        rem = val % self.capacity
                
        # case 1: linked list為空

        if self.data[rem] == None:
            pass

        # case 2: val在head

        elif self.data[rem].val == val:
            self.data[rem] = self.data[rem].next

        #case 3: val不在head 且 next為空

        else:
            if self.data[rem].next == None:
                pass
            else:
                prev = self.data[rem]
                remo = self.data[rem].next
                while remo != None and remo.val != val:
                    prev = remo
                    remo = remo.next

        #case 3-1: val不在head 也找不到          

                if remo == None:
                    pass 

        #case 3-2: val在某個非head的位置

                else:
                    prev.next = remo.next
                    remo = None
                        
    def contains(self,key):
        a = MD5.new()
        a.update(key.encode("utf-8"))
        val = int(a.hexdigest(),16)
        rem = val % self.capacity
        
        # case 1: linked list為空
                
        if self.data[rem] == None:
            return False

        # case 2: val在head

        elif self.data[rem].val == val:
            return True

        #case 3: val不在head 且 next為空

        else:
            if self.data[rem].next == None:
                return False
            else:
                prev = self.data[rem]
                remo = self.data[rem].next
                while remo != None and remo.val != val:
                    prev = remo
                    remo = remo.next

        #case 3-1: val不在head 也找不到          

                if remo == None:
                    return False 

        #case 3-2: val在某個非head的位置

                else:
                    return True
                    
    def pre(self):
        for i in range(self.capacity):
            temp = self.data[i]
            count = 0
            while temp is not None:
                print("linked list",i,"index =",count," = ",temp.val)
                temp = temp.next
                count += 1

#參考資料:

#https://www.youtube.com/watch?v=aZVNWYSR_sY

#https://www.youtube.com/watch?v=2BldESGZKB8

#https://github.com/timvandermeij/md5.py/blob/master/md5.py

#http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html

#https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view
