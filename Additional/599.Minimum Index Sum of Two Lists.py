class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp = []
        comb = []
        ans = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    temp.append(i)
                    comb.append(i+j)

        for i in range(len(comb)):
            if comb[i] == min(comb):
                ans.append(list1[temp[i]])
        return ans
