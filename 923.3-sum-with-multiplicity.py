#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

# @lc code=start


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        Mod = 10 ** 9 + 7
        Max = 100
        d = dict.fromkeys(A, 0)
        a = set(A)
        l = len(a)
        ans = 0
        for x in A:
            d[x] += 1
        for i in range(target + 1):
            for j in range(i, target + 1):
                k = target - i - j
                if k < 0 or k > Max or k < j:
                    continue
                if k not in d or i not in d or j not in d:
                    continue
                if i == j == k:
                    ans += (d[i] - 2) * (d[i] - 1) * d[i] / 6
                elif i == j and j != k:
                    ans += d[i] * (d[i] - 1) / 2 * d[k]
                elif i != j and j == k:
                    ans += d[i] * (d[j] - 1) * d[j] / 2
                else:
                    ans += d[i] * d[j] * d[k]
        return int(ans % Mod)

# @lc code=end
