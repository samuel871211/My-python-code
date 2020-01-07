class Solution:
    def wordPattern(self, a: str, b: str) -> bool:
        b = b.split(" ")
        final_1 = {}
        final_2 = {}
        temp = set()
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] not in final_1 and b[i] not in final_2:
                temp.add(b[i])
                final_1[a[i]] = temp
                temp = set()
                temp.add(a[i])
                final_2[b[i]] = temp
                temp = set()
            else:
                if a[i] in final_1:
                    final_1[a[i]].add(b[i])
                    if len(final_1[a[i]]) > 1:
                        return False
                elif b[i] in final_2:
                    final_2[b[i]].add(a[i])
                    if len(final_2[b[i]]) > 1:
                        return False
        return True
