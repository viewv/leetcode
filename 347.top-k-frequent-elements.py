#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict.fromkeys(nums, 0)
        for x in nums:
            d[x] += 1
        d = d.items()
        d = sorted(d, key=lambda x: x[1], reverse=True)
        return [x[0] for x in d[:k]]
