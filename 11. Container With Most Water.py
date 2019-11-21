class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        n = len(height)
        i = 0
        j = n - 1
        while i < j:
            if height[i] <= height[j]:
                area = height[i] * (j - i)
                i += 1
            else:
                area = height[j] * (j - i)
                j -= 1
            if area > maxarea:
                maxarea = area
        return maxarea
