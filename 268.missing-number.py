#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = s = 0
        for x in nums:
            l += 1
            s += x
        s = l * (l + 1) // 2 - s
        return s


# @lc code=end
