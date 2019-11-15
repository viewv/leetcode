#
# @lc app=leetcode id=754 lang=python3
#
# [754] Reach a Number
#

# @lc code=start


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        s = k = 0
        while s < target:
            k += 1
            s += k
        d = s - target
        if d % 2 == 0:
            return k
        return k + 1 + k % 2


# @lc code=end
