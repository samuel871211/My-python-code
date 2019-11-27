class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = sorted(arr)
        b = [0]
        for i in range(len(a)-1):
            if a[i] != a[i+1]:
                b.append(i+1)
        b.append(len(a))
        for j in range(len(b)-1):
            b[j] = b[j+1]-b[j]
        b.pop(-1)
        if len(set(b)) == len(b):
            return True
        else:
            return False
