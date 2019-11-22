#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list()
        for x in s:
            if x.isalpha() or x.isalnum():
                l.append(x.lower())
        length = len(l)
        i = 0
        j = length - 1
        while i <= j:
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1
        return True


# @lc code=end
