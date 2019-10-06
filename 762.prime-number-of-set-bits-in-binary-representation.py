#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        ans = 0
        s = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
        for x in range(L, R + 1):
            num = bin(x).count('1')
            if s[num] == 1:
                ans += 1
        return ans

# @lc code=end
