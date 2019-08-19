#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#


class Solution:
    def _tonum(self, n):
        ans = 0
        times = 1
        l = len(n)
        for x in range(l - 1, -1, -1):
            ans += int(n[x]) * times
            times *= 10
        return ans

    def addStrings(self, num1: str, num2: str) -> str:
        num1 = self._tonum(num1)
        num2 = self._tonum(num2)
        num = num1 + num2
        return str(num)
