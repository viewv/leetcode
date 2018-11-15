class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = end = area = 0
        maxlen = len(height)
        while end < maxlen:
            if height[end] >= height[start]:
                for x in range(start, end):
                    area += height[start] - height[x]
                start = end
                end = start + 1
            else:
                end += 1
        return area


sol = Solution()

print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
