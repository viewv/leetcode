class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ans = 1 << 32
        path = 1
        flag = 0
        n = len(grid)
        curr = [0, 0]
        if grid[curr[0]][curr[1]] == 1:
            return -1
        dic = [[0, -1], [0, 1], [-1, 0], [1, 0],
               [1, -1], [1, 1], [-1, -1], [-1, 1]]

        def testnext(curr, head):
            x = curr[0] + head[0]
            y = curr[1] + head[1]
            if x < 0 or x >= n or y < 0 or y >= n:
                return False
            if grid[x][y] == 1:
                return False
            if grid[x][y] - 2 == 0 or grid[x][y]-2 == 1:
                return False
            return True

        def testall(curr):
            for head in dic:
                if testnext(curr, head):
                    return True
            return False

        def dfs(curr):
            if not testall(curr):
                if curr[0] == n - 1 and curr[1] == n - 1:
                    nonlocal path
                    nonlocal ans
                    nonlocal flag
                    flag = 1
                    if path < ans:
                        ans = path
                return
            if path >= ans:
                return
            for head in dic:
                if testnext(curr, head):
                    curr[0] += head[0]
                    curr[1] += head[1]
                    grid[curr[0]][curr[1]] += 2
                    path += 1
                    dfs(curr)
                    grid[curr[0]][curr[1]] -= 2
                    path -= 1
                    curr[0] -= head[0]
                    curr[1] -= head[1]
            return
        grid[0][0] += 2
        dfs([0, 0])
        if flag == 0:
            return -1
        else:
            return ans
#!TLE