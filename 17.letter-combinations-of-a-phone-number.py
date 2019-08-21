#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        digits = [int(x) for x in list(digits)]
        if length == 0:
            return []
        d = [0, 1, [3, 'a', 'b', 'c'], [3, 'd', 'e', 'f'], [3, 'g', 'h', 'i'],
             [3, 'j', 'k', 'l'], [3, 'm', 'n', 'o'], [4, 'p', 'q', 'r', 's'],
             [3, 't', 'u', 'v'], [4, 'w', 'x', 'y', 'z']]
        res = d[digits[0]][1:]
        digits = digits[1:]
        for i, x in enumerate(digits):
            alpha = d[int(x)]
            num, alpha = alpha[0], alpha[1:]
            temp = []
            for n in res:
                for j in range(num):
                    word = n + alpha[j]
                    temp.append(word)
            res = temp
        return res
