class Solution(object):
    
    def merge_sort(self,nums): #進行split的步驟，之後把呼叫merge函式，把nums,left,right傳給它，最後回傳merge過後的結果
        
        self.nums = nums
        
        left = nums[0:len(nums)//2]
        right = nums[len(nums)//2:len(nums)]
    
        if len(left) > 1:
            Solution().merge_sort(left)
    
        if len(right) > 1:
            Solution().merge_sort(right)
        
        SortedArray = Solution().merge(nums,left,right)
        return SortedArray
    
    def merge(self,nums,left,right): #非使用者能呼叫的函式，這是主要merge邏輯判斷的底層函式，使用者僅能呼叫merge_sort
    
        index_left = 0
        index_right = 0
        index_nums = 0
    
        while index_left < len(left) and index_right < len(right): 
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
    
        while index_left < len(left) and index_right == len(right): 
            nums[index_nums] = left[index_left]
            index_left = index_left + 1
            index_nums = index_nums + 1
   
        while index_right < len(right) and index_left == len(left): 
            nums[index_nums] = right[index_right]
            index_right = index_right + 1
            index_nums = index_nums + 1

        return nums
