class Solution:
    def myPow(self, x, n):
        y = 1
        while True:
            t = n % 2
            n = n // 2
            if t == 1:
                y = y * x
            if n == 0:
                break
            x = x * x
        return y

solobj = Solution()

print(solobj.myPow(2,10))