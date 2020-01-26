class Solution:
    def myAtoi(self, a: str) -> int:
        if len(a) == 0:
            return 0
        if len(a) == 1:
            if a[0].isdigit() == True:
                return int(a)
            return 0
        while a[0] == " ":
            a = a[1:]
            if len(a) == 0:
                return 0
        if a[0] == "-" or a[0] == "+" or a[0].isdigit() == True:
            i = 1
            while i < len(a) and a[i].isdigit() == True:
                i += 1
            if i == 1:
                if a[0].isdigit() == True:
                    return int(a[0])
                return 0
            if int(a[:i]) > 2147483647:
                return 2147483647
            if int(a[:i]) < -2147483648:
                return -2147483648
            return int(a[:i])           
        if a[0] != "-" or a[0] != "+" or a[0].isdigit() == False:
            return 0
