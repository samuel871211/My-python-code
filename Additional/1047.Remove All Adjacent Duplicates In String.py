class Solution:
    def removeDuplicates(self, S: str) -> str:
        b = list(S)
        curlen = len(b) - 1
        det = True
        for i in range(len(b)-1):      
            if i < curlen:
                if b[i] == b[i+1]:
                    b.pop(i)
                    b.pop(i)
                    curlen -= 2
                    det = False
        if det == True:
            return S
        else:
            c = "".join(b)
            if c == "" or len(c) == 1:
                return c
            else:
                return Solution().removeDuplicates(c)
