#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start

from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []

        def back(t):
            if t == N:
                temp = []
                for x in range(0, N):
                    temp.append(nums[x])
                ans.append(temp)
            else:
                for x in range(t, N):
                    temp = nums[x]
                    nums[x] = nums[t]
                    nums[t] = temp
                    back(t+1)
                    temp = nums[x]
                    nums[x] = nums[t]
                    nums[t] = temp
        back(0)
        return ans


# @lc code=end
