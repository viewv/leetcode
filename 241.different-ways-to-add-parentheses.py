#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start

import itertools
from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y}

        def ways(s):
            ans = []
            l = len(s)
            for i in range(l):
                if s[i] in '-+*':
                    ans += [op[s[i]](l, r)
                            for l, r in itertools.product(ways(s[0:i]), ways(s[i + 1:]))]
            if not ans:
                ans.append(int(s))
            return ans
        return ways(input)
# @lc code=end
