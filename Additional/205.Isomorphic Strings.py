class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(set(s)) != len(set(t)): return False

        arr = sorted(list(zip(s,t)))
        for i in range(len(arr)-1):
            if arr[i][0] == arr[i+1][0]:
                if arr[i][1] != arr[i+1][1]: return False
        return True
