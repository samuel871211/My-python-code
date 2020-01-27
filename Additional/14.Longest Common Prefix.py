class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        pivot = sorted(strs)[0]
        if len(pivot) == 0:
            return ""
        for i in range(len(pivot)):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    if i == 0:
                        return ""
                    return pivot[:i]
        return pivot
