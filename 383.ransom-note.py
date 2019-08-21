#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        d = dict.fromkeys(magazine, 0)
        for x in magazine:
            d[x] += 1
        for x, s in enumerate(ransomNote):
            if s not in d:
                return False
            elif d[s] == 0:
                return False
            else:
                d[s] -= 1
        return True
