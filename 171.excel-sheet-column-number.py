#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start


class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        i = 0
        ans = 0
        for x in s:
            ans += (ord(x) - 64) * (26 ** i)
            i += 1
        return ans

# @lc code=end
