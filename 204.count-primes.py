#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start


class Solution:

    def countPrimes(self, n: int) -> int:
        ans = 0
        IsPrime = [True] * (n)
        for i in range(2, int(n ** 0.5) + 1):
            if IsPrime[i]:
                for j in range(i * i, n, i):
                    IsPrime[j] = False
        for x in range(2, n):
            if IsPrime[x]:
                ans += 1
        return ans
        # @lc code=end
