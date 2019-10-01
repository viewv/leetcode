class Solution:

    def gcd(self, a, b):
        while a != b:
            a, b = ((a - b), b) if a > b else ((b - a), a)
        return a

    def lcm(self, a, b):
        return a*b//self.gcd(a, b)

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l = 1
        r = 2 * 10 ** 9
        ab = self.lcm(a, b)
        ac = self.lcm(a, c)
        bc = self.lcm(b, c)
        abc = self.lcm(a, bc)
        while l < r:
            m = (l + r - 1) // 2
            k = m//a + m//b + m//c - m//ab - m//bc - m//ac + m//abc
            r, l = (m, l) if k >= n else (r, m+1)
        return l
