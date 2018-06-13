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


num = input('Please input!')
num = num.split()
a = int(num[0])
b = int(num[1])

print(solobj.myPow(a,b))