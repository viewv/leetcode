class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        n = len(height)
        for x in range(n-1):
            area = 0
            temp = height[x]
            for y in range(x + 1, n):
                if height[y] >= temp:
                    area += temp
            if area > maxarea:
                maxarea = area
        return maxarea
