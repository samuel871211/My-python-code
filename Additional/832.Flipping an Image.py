class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        b = []
        for i in A:
            b.append(i[::-1])
        for i in range(len(b)):
            for j in range(len(b[i])):
                if b[i][j] == 0:
                    b[i][j] = 1
                else:
                    b[i][j] = 0
        return b
