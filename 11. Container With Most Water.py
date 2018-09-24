class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        flag = 0
        length = len(height)
        a = 0
        b = 0
        tmp = 0
        for x in range(0, length):
            if height[x] >= height[flag]:
                a = height[x]
                b = 0
                for y in range(x + 1, length):
                    b += 1
                    if height[y] <= a:
                        tmp = height[y]
                        if tmp * b > area:
                            area = tmp * b
                            a = height[y]
                flag = x
        return area
