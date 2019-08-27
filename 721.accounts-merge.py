#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        data = [[[]] for x in range(26)]
        for x in accounts:
            name = x[0]
            emails = x[1:]
            order = ord(name[0]) - 65
            group = data[order]
            for y in group:
                

