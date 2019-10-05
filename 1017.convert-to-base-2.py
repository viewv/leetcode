#
# @lc app=leetcode id=1017 lang=python3
#
# [1017] Convert to Base -2
#

# @lc code=start

# import math


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


# @lc code=end
