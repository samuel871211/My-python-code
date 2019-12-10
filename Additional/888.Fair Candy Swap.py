class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sc = sum(B)-sum(A)
        b = set(B)
        for i in A:
            k = (sc+2*i)/2
            if k in b:
                return [i,k]
