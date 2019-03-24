# def minPathSum(grid):
#     """
#     :type grid: List[List[int]]
#     :rtype: int
#     """
#     nc = len(grid)
#     nr = len(grid[0])
#     for x in range(1, nr):
#         grid[0][x] += grid[0][x-1]
#     for x in range(1, nc):
#         grid[x][0] += grid[x-1][0]
#         for y in range(1, nr):
#             grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])

#     return grid[nc-1][nr-1]


# grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

# print(minPathSum(grid))

# def uniquePaths(m, n):
#     """
#     :type m: int
#     :type n: int
#     :rtype: int
#     """
#     grid = [[0 for x in range(n)] for x in range(m)]
#     for x in range(m-1, -1, -1):
#         for y in range(n-1, -1, -1):
#             if x == m-1 and y == n - 1:
#                 grid[x][y] = 1
#             elif y == m - 1:
#                 grid[x][y] = grid[x][y + 1]
#             else:
#                 grid[x][y] = grid[x+1][y]+grid[x][y+1]
#     return grid[0][0]


# print(uniquePaths(7, 3))

def uniquePaths(m, n):
    dp = [[1 for x in range(m)] for y in range(n)]
    for x in range(1, n):
        for y in range(1, m):
            dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
    return dp[n-1][m-1]


print(uniquePaths(3, 2))
