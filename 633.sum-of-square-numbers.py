#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        m = int(c ** 0.5+1)
        for x in range(m):
            if math.sqrt(c - x * x).is_integer():
                return True
        return False


# @lc code=end
