class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nc = len(grid)
        nr = len(grid[0])
        for x in range(1, nr):
            grid[0][x] += grid[0][x-1]
        for x in range(1, nc):
            grid[x][0] += grid[x-1][0]
            for y in range(1, nr):
                grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])

        return grid[nc-1][nr-1]
