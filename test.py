def gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        q, r = a//b, a % b
        s, t = gcd(b, r)
        return (t, s-q*t)


ans = gcd(3533, 11200)
print(ans)
# print(gcd(435 ** 765, 2579))
