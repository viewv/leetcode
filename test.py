def gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        q, r = a//b, a % b
        s, t = gcd(b, r)
        return (t, s-q*t)


print(gcd(3, 11))
# print(gcd(435 ** 765, 2579))
