from typing import List


from itertools import product, compress


# sol = Solution()
# print(sol.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000))

# def gcd(a, b):
#     while a != b:
#         a, b = ((a - b), b) if a > b else ((b - a), a)
#     return a


# print(gcd(5, 10))

# import math


# class Solution:
#     def baseNeg2(self, N: int) -> str:
#         number_list = []
#         if N == 0:
#             return '0'
#         while N != 0:
#             k = math.ceil(N / -2)
#             r = N - k * (-2)
#             number_list.append(r)
#             N = k
#         number = ''.join([str(x) for x in number_list[::-1]])
#         return number


# sol = Solution()
# print(sol.baseNeg2(100))

# import math
# from decimal import Decimal


# class Solution:
#     def findRepeat(self, S: str):
#         start = end = 0
#         pointflag = 0
#         for i, x in enumerate(S):
#             if x == '(':
#                 start = i + 1
#             if x == ')':
#                 end = i
#                 break
#             if x == '.':
#                 pointflag = 1
#         if pointflag == 0:
#             return float(S)
#         repeat = S[start:end]
#         add = [repeat for x in range(16)]
#         add = ''.join(add)
#         num = Decimal(S[:start - 1] + add)
#         return num

#     def isRationalEqual(self, S: str, T: str) -> bool:
#         num_s = self.findRepeat(S)
#         print(num_s)
#         num_t = self.findRepeat(T)
#         print(num_t)
#         print(abs(num_s-num_t))
#         return bool(abs(num_s - num_t) <= 10 ** -7)

# class Solution:

#     def divminu(self, da, db):
#         return {'up': da['up']*db['down']-db['up']*da['down'], 'down': da['down']*db['down']}

#     def divplus(self, da, db):
#         return {'up': da['up']*db['down']+db['up']*da['down'], 'down': da['down']*db['down']}

#     def divsion(self, da, db):
#         return {'up': da['up'] * db['down'], 'down': da['down'] * db['up']}

#     def getDiv(self, s):
#         start = end = pointflag = 0
#         length = len(s)
#         for i, x in enumerate(s):
#             if x == '.':
#                 pointflag = i
#             if x == '(':
#                 start = i
#             if x == ')':
#                 end = i
#         if pointflag == 0:
#             return {'up': int(s), 'down': 1}
#         elif start == end and start == 0:
#             width = length - pointflag - 1
#             real = s[:pointflag]
#             less = s[pointflag + 1:]
#             if less == '':
#                 return {'up': int(real), 'down': 1}
#             else:
#                 return self.divplus({'up': int(real), 'down': 1}, {'up': int(less), 'down': 10**width})

#         else:
#             width = end - pointflag - 2
#             down = 10 ** width
#             repeat = int(s[start + 1:end])
#             up = repeat
#             real = self.getDiv(s[:start])
#             length = end - start - 1
#             a1 = {'up': up, 'down': down}
#             q = {'up': 1, 'down': 10 ** length}
#             one = {'up': 1, 'down': 1}
#             res = self.divplus(self.divsion(a1, self.divminu(one, q)), real)
#             return res

#     def isRationalEqual(self, S: str, T: str) -> bool:
#         div_a = self.getDiv(S)
#         div_b = self.getDiv(T)
#         div = self.divminu(div_a, div_b)
#         return bool(div['up'] == 0)


# sol = Solution()
# print(sol.isRationalEqual("0.08(9)", "0.09"))

# from typing import List


# class Solution:
#     def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
#         d = [int(x) for x in D]
#         s = set(d)
#         l = [0 for x in range(11)]
#         for x in d:
#             for y in range(x, 11):
#                 l[y] += 1
#         ans = 0
#         num = [int(x) for x in list(str(N))]
#         length = len(num)
#         count = len(s)
#         for i in range(length):
#             if num[i] not in s:
#                 for j in range(l[num[i]]):
#                     ans += count ** (length - i - 1)
#             else:
#                 for j in range(l[num[i]] - 1):
#                     ans += count ** (length - i - 1)
#                 temp = 1
#                 for j in range(i + 1, length):
#                     temp *= l[num[j]]
#                 ans += temp
#             for k in range(i + 1, length):
#                 num[k] = 9
#         return ans

# from typing import List


# class Solution:
#     def sumSubseqWidths(self, A: List[int]) -> int:
#         p = 1
#         ans = 0
#         A = sorted(A)
#         n = len(A)
#         Mod = 10 ** 9 + 7
#         for i in range(n):
#             ans += (A[i] - A[n - i - 1]) * (p % Mod)
#             p = p << 1 % Mod
#         return ans % Mod

# class Solution:
#     def countPrimeSetBits(self, L: int, R: int) -> int:
#         ans = 0
#         s = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
#         for x in range(L, R + 1):
#             num = bin(x).count('1')
#             if s[num] == 1:
#                 ans += 1
#         return ans

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        now = nums[0]
        times = 1
        l = len(nums)
        for x in range(1,l):
            if nums[x] == now:
                times += 1
            if nums[x] != now:
                if times == 1:
                    return now
                else:
                    times = 1
                    now = nums[x]
        return now


sol = Solution()

print(sol.singleNonDuplicate([1]))
