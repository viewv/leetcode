class Solution:
    def tonNum(self, a):
        ans = 0
        a = a[::-1]
        for i, c in enumerate(a):
            ans += c * (2 ** i)
        return ans

    def threeEqualParts(self, A: List[int]) -> List[int]:
        i, j = 0, 1
        l = len(A)
        a, b, c = 0, A[1], self.tonNum(A[j+1:])
        for i in range(0, l-1):
            j = i+1
            a = (a << 1) + A[i]
            b = A[j]
            c = c & (2 ** (l - j - 1) - 1)
            sc = c
            for j in range(i + 1, l-1):
                if a == b and b == sc:
                    return [i, j + 1]
                else:
                    b = (b << 1) + A[j + 1]
                    sc = sc & (2 ** (l - j - 2) - 1)
        return [-1, -1]
        
#! Pass 94/104
