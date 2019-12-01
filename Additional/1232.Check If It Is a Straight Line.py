class Solution:
    def checkStraightLine(self, a: List[List[int]]) -> bool:
        for i in range(1,len(a)-1):
            if a[i][0]-a[0][0] == 0 and a[i+1][0]-a[0][0] != 0:
                return False
            elif a[i][0]-a[0][0] != 0 and a[i+1][0]-a[0][0] != 0:
                if (a[i][1]-a[0][1])/(a[i][0]-a[0][0]) != (a[i+1][1]-a[0][1])/(a[i+1][0]-a[0][0]):
                    return False
        return True
