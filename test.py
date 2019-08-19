from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        part = sum(nums)
        if part % 2 == 0:
            part = part // 2
        else:
            return False
        row = len(nums) + 1
        col = part + 1
        s = [[0 for c in range(col)] for r in range(row)]
        s[0][0] = 1
        for i in range(1, col):
            s[0][i] = 0
        for j in range(1, row):
            s[j][0] = 1
            for k in range(1, col):
                s[j][k] = s[j - 1][k]
                if s[j][k] == 1:
                    s[j][k] = s[j][k]
                elif (k - nums[j - 1] >= 0) and (s[j-1][k - nums[j - 1]] == 1):
                    s[j][k] = s[j-1][k - nums[j - 1]]
                else:
                    s[j][k] = 0
                if k == col - 1 and s[j][k] == 1:
                    return True
        return False


sol = Solution()
print(sol.canPartition([1, 2, 5]))
