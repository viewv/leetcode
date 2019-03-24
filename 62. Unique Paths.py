class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1 for x in range(m)] for y in range(n)]
        for x in range(1, n):
            for y in range(1, m):
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        return dp[n-1][m-1]
