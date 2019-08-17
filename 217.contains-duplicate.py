#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 0:
            return False
        s = set()
        for x in nums:
            if x in s:
                return True
            else:
                s.add(x)
        return False
