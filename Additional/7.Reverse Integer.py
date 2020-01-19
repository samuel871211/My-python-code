class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)[::-1]
        if a[-1] == "-":
            a = "-" + a[:-1]
            while a[1] == "0":
                a = a[0] + a[2:]
            if int(a) > 2147483647 or int(a) < -2147483648:
                return 0
            return a
        while a[0] == "0" and len(a) > 1:
            a = a[1:]
        if int(a) > 2147483647 or int(a) < -2147483648:
            return 0
        return a
