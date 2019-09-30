'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [[x, i] for i, x in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[0])
        start = 0
        end = len(nums) - 1
        while start <= end:
            s = nums[start][0] + nums[end][0]
            if s > target:
                end -= 1
            if s < target:
                start += 1
            if s == target:
                return [nums[start][1], nums[end][1]]
