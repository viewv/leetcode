class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        s = []
        for x in matrix:
            s += x
        s = sorted(s)
        return s[k-1]
