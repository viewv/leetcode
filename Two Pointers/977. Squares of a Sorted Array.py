class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = sorted([x*x for x in A])
        return A
