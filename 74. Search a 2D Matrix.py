class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        s = []
        for x in matrix:
            s += x
        for x in s:
            if x == target:
                return True
        return False