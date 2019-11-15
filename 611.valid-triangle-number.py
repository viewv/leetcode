#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 3:
            return 0
        nums = sorted(nums, reverse=True)
        ans = 0
        for x in range(0, l - 2):
            a, b = l - 1, x + 1
            while a > b:
                if nums[a] + nums[b] > nums[x]:
                    ans += (a - b + 1)-1
                    b += 1
                else:
                    a -= 1
        return ans


# @lc code=end
