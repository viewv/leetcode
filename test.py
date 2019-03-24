def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or not obstacleGrid[0]:
        return 0
    if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
        return 0
    m = len(obstacleGrid[0])
    n = len(obstacleGrid)
    dp = [[1 for x in range(m)] for y in range(n)]
    for x in range(1, n):
        for y in range(1, m):
            if obstacleGrid[x][y] == 1:
                dp[x][y] = 0
                continue
            else:
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
    return dp[n-1][m-1]


print(uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
