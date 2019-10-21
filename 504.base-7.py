#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start


class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = 0
        if num < 0:
            flag = 1
        num = abs(num)
        s = ""
        while num >= 0:
            s += str(num % 7)
            num = num//7
            if num == 0:
                break
        return flag*"-"+s[::-1]
# @lc code=end
