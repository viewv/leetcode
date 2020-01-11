class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        tri = [0, 1, 1]
        i = 3
        while i < n:
            temp = tri[i - 1] + tri[i - 2] + tri[i-3]
            tri.append(temp)
            i += 1
        return tri[i-1] + tri[i-2] + tri[i-3]
