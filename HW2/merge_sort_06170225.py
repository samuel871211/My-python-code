class Solution(object):
    
    def merge_sort(self,nums): #merge_sort是給使用者呼叫的函式，會將輸入的nums進行split，之後再呼叫merge，最後再return排列好的nums
        
        self.nums = nums
        
        left = nums[0:len(nums)//2]
        right = nums[len(nums)//2:len(nums)]
    
        if len(left) > 1:
            Solution().merge_sort(left)
    
        if len(right) > 1:
            Solution().merge_sort(right)
        
        SortedArray = Solution().merge(nums,left,right)
        return SortedArray
    
    def merge(self,nums,left,right): #merge會接收split完的nums,left,right來進行合併動作，最後return排列好的nums，但使用者不會直接用到這函式
    
        index_left = 0
        index_right = 0
        index_nums = 0
    
        while index_left < len(left) and index_right < len(right): #當左右計數都小於本身長度，可以安心的進行比較
            if left[index_left] < right[index_right]:
                nums[index_nums] = left[index_left]
                index_left = index_left + 1
            elif left[index_left] > right[index_right]:
                nums[index_nums] = right[index_right]
                index_right = index_right + 1
            elif left[index_left] == right[index_right]:
                nums[index_nums] = left[index_left]
                index_left = index_left + 1           
            index_nums = index_nums + 1  
    
        if index_left < len(left) and index_right == len(right): #右計數超過本身長度，把left剩下的值依序塞入nums
            for i in range(index_left,len(left)):
                nums[index_nums] = left[index_left]
                index_left = index_left + 1
                index_nums = index_nums + 1
        elif index_right < len(right) and index_left == len(left): #左計數超過本身長度，把right剩下的值依序塞入nums
            for i in range(index_right,len(right)):
                nums[index_nums] = right[index_right]
                index_right = index_right + 1
                index_nums = index_nums + 1

#             while index_left < len(left) and index_right == len(right): 
#                 nums[index_nums] = left[index_left]
#                 index_left = index_left + 1
#                 index_nums = index_nums + 1
#while迴圈是當statement true，會"重複執行"裡面的程式碼，可以用在"不確定要執行幾次的時候"
#可是今天我很清楚，當left已經跑完，right剩下的值依序塞入nums要執行range(index_right,len(right))次
#所以我可以把while改成if包for的判斷式，一樣能達到同樣的效果
#邏輯通了寫起來94爽==

#             while index_right < len(right) and index_left == len(left):
#                 nums[index_nums] = right[index_right]
#                 index_right = index_right + 1
#                 index_nums = index_nums + 1

        return nums
