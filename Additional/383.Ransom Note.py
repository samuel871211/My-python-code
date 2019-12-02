class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        for i in set(a):
            if i not in b:
                return False
            else:
                if a.count(i) > b.count(i):
                    return False
        return True
