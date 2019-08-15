from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        length = len(A)
        lplu = [0 for x in range(length)]
        lmin = [0 for x in range(length)]
        maxnum = 0
        for x in range(0, length):
            lplu[x] = A[x] + x
            lmin[x] = A[x] - x
        for x in range(length - 1):
            start = lplu[x]
            end = max(lmin[x + 1:])
            if start + end >= maxnum:
                maxnum = start + end
        return maxnum
