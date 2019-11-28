class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        arr4 = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    arr3.append(arr2[i])
        for i in arr1:
            if i not in arr3:
                arr4.append(i)
        arr4 = sorted(arr4)
        arr3.extend(arr4)
        return arr3
