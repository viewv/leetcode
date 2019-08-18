#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#


class Solution:
    def _maxlim(self, num):
        res = num // 2
        while res > 1:
            if num % res == 0:
                return [res, num // res]
            res -= 1
        return [1, num]

    def minSteps(self, n):
        res, times = self._maxlim(n)
        if n == 1:
            return 0
        if n == 2:
            return 2
        if n == 3:
            return 3
        if res == 1:
            return n
        else:
            dp = [0 for x in range(n+1)]
            dp[1] = 0
            dp[2] = 2
            dp[3] = 3
            for x in range(4, n + 1):
                r, t = self._maxlim(x)
                if r == 1:
                    dp[x] = x
                else:
                    dp[x] = dp[r] + t
            return dp[n]
