#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#


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
        for i in range(1, col):
            s[0][i] = 0
        for j in range(1, row):
            s[j][0] = 1
            for k in range(1, col):
                s[j][k] = s[j - 1][k]
                if s[j][k] != 1 and (k - nums[j - 1] >= 0) and (s[j - 1][k - nums[j - 1]] == 1):
                    s[j][k] = s[j - 1][k - nums[j - 1]]
                if k == col - 1 and s[j][k] == 1:
                    return True
        return False

# 子集和问题
# dp[i,w] = dp[i-1,w]||dp[i-1][w-nums[i]]
# dp[i,w] 代表在前i个元素中是否存在子集和等于w
# 第一种情况在i之前就有了，不选择i，有dp[i-1,w]
# 第二种情况在i之前还没有，选择i，测试dp[i-1,w-nums[i]]
# 测试是否i前面的子集存在能够不出残缺的集合，最后求或得解
