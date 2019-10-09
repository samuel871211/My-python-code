class Solution: #假設nums=[1,2,2,4]
    def findErrorNums(self, nums: List[int]) -> List[int]: #nums這個list裡面放int，return結果也是一樣
        finalAnswer = [] #放重複值跟缺失值
        sort = [] #放原本正確的list
        double = sum(nums) - sum(set(nums)) #set是集合，會把list的重複值刪掉 (1+2+3+4)-(1+2+4)=2=重複值
        for i in range(0,len(nums)): #迴圈執行4次
            sort.append(i) #這邊的sort=[1,2,3,4]
        non = list(set(sort)-set(nums)) #non=[缺失值]=[3]
        finalAnswer.append(double) #把重複值append進去   
        finalAnswer.append(non[-1]) #把缺失值append進去 這邊也可以寫成finalAnswer.extend(non)
        return finalAnswer
