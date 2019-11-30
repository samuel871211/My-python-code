class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        temp = []
        for i in S:
            if i.isalpha():
                temp.append(i)
        r = temp[::-1]
        for i in range(len(S)):
            if S[i].isalpha():
                S[i] = r[0]
                r.pop(0)
        final = "".join(S)
        return final
