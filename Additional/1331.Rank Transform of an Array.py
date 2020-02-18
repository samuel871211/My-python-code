class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return []
        ans = sorted(list(zip(arr,(i for i in range(len(arr))))))
        arr[ans[0][1]] = 1
        if len(arr) > 1:
            for i in range(1,len(ans)):
                if ans[i][0] != ans[i-1][0]:
                    arr[ans[i][1]] = arr[ans[i-1][1]] + 1
                else:
                    arr[ans[i][1]] = arr[ans[i-1][1]]
        return arr
