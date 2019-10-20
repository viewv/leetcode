#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start


class Solution:
    def test(self, num: int):
        nums = [int(x) for x in str(num)]
        for x in nums:
            if x == 0 or num % x != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        number = [x for x in range(left, right + 1)]
        ans = []
        for x in number:
            if self.test(x):
                ans.append(x)
        return ans


# @lc code=end
