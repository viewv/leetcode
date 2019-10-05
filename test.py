
# from typing import List


# class Solution:
#     def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
#         flag_zero = 'z'
#         flag_one = 'o'
#         number_prison = len(cells)
#         for x in range(N):
#             past = [x for x in cells]
#             cells[0] = flag_zero
#             cells[number_prison - 1] = flag_zero
#             for i in range(1, number_prison - 1):
#                 if past[i - 1] == past[i + 1]:
#                     cells[i] = flag_one
#                 else:
#                     cells[i] = flag_zero
#             for i, c in enumerate(cells):
#                 if c == flag_one:
#                     cells[i] = 1
#                 else:
#                     cells[i] = 0
#         return cells


# sol = Solution()
# print(sol.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000))

# def gcd(a, b):
#     while a != b:
#         a, b = ((a - b), b) if a > b else ((b - a), a)
#     return a


# print(gcd(5, 10))

import math


class Solution:
    def baseNeg2(self, N: int) -> str:
        number_list = []
        if N == 0:
            return '0'
        while N != 0:
            k = math.ceil(N / -2)
            r = N - k * (-2)
            number_list.append(r)
            N = k
        number = ''.join([str(x) for x in number_list[::-1]])
        return number


sol = Solution()
print(sol.baseNeg2(100))
