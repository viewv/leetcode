#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = dict.fromkeys(words, 0)
        for x in words:
            d[x] -= 1
        l = list(d.items())
        l = sorted(l, key=lambda x: (x[1], x[0]))
        l = [x[0] for x in l[:k]]
        return l
