from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        l = []
        for i, x in enumerate():
            l.append([x, i])
        l = sorted(l, key=lambda x: x[0])
        