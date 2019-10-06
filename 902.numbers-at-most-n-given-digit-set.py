#
# @lc app=leetcode id=902 lang=python3
#
# [902] Numbers At Most N Given Digit Set
#

# @lc code=start


class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        s = str(N)
        n = len(s)
        ans = sum(len(D) ** i for i in range(1, n))
        for i, c in enumerate(s):
            ans += len(D) ** (n - i - 1) * sum(d < c for d in D)
            if c not in D:
                return ans
        return ans + 1
# @lc code=end
