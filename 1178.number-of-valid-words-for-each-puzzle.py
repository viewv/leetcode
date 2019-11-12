#
# @lc app=leetcode id=1178 lang=python3
#
# [1178] Number of Valid Words for Each Puzzle
#

# @lc code=start


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ans = []
        freq = dict()
        for word in words:
            mask = 0
            for c in word:
                mask = mask | (1 << (ord(c) - 97))
            if mask not in freq:
                freq[mask] = 0
            freq[mask] += 1
        for p in puzzles:
            total = 0
            l = len(p) - 1
            for i in range(0, 1 << l):
                mask = 1 << (ord(p[0]) - 97)
                for j in range(0, l):
                    if i & (1 << j):
                        mask = mask | (1 << (ord(p[j + 1]) - 97))
                if mask in freq:
                    total += freq[mask]
            ans.append(total)
        return ans


# @lc code=end
