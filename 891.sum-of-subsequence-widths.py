#
# @lc app=leetcode id=891 lang=python3
#
# [891] Sum of Subsequence Widths
#

# @lc code=start


class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        p = 1
        ans = 0
        A = sorted(A)
        n = len(A)
        Mod = 10 ** 9 + 7
        for i in range(n):
            ans += (A[i] - A[n - i - 1]) * (p % Mod)
            p = p << 1 % Mod
        return ans % Mod

# @lc code=end
