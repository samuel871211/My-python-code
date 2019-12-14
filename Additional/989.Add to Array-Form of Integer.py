class Solution:
    def addToArrayForm(self, a: List[int], k: int) -> List[int]:
        k = str(k)
        c = len(a)
        d = len(k)
        ans = []
        for i in range(1,min(c,d)+1):
            ans.insert(0,a[-i]+int(k[-i]))
        for i in range(min(c,d)+1,max(c,d)+1):
            if c == max(c,d):
                ans.insert(0,a[-i])
            else:
                ans.insert(0,int(k[-i]))
        ans.insert(0,0)
        for i in range(1,len(ans)):
            if ans[-i] >= 10:
                ans[-i] -= 10
                ans[-i-1] += 1
        if ans[0] == 0:
            ans.remove(0)
        return ans
