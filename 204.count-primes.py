#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start


class Solution:
    def test(self, n):
        if n in (2, 3):
            return True
        flag = int(n ** 0.5)
        for x in range(2, flag + 1):
            if n % x == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        nums = [x for x in range(n)]
        ans = 0
        for x in range(2, n):
            if nums[x] != 0 and self.test(nums[x]):
                ans += 1
                k = 2
                temp = k * x
                while temp < n:
                    nums[temp] = 0
                    k += 1
                    temp = k * x
        return ans
        # @lc code=end
