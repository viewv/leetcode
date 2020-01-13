class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        lx = len(grid)
        ly = len(grid[0])
        maxgold = 0
        mined = []
        locmap = [[0 for x in y] for y in grid]
        heads = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def testnext(curr, head):
            x = curr[0] + head[0]
            y = curr[1] + head[1]
            if x < 0 or y < 0:
                return False
            if x >= lx or y >= ly:
                return False
            if locmap[x][y] == 1:
                return False
            if grid[x][y] == 0:
                return False
            return True

        def testallnext(curr):
            for head in heads:
                if testnext(curr, head):
                    return True
            return False

        def dfs(curr):
            if not testallnext(curr):
                temp = sum(mined)
                nonlocal maxgold
                if temp > maxgold:
                    maxgold = temp
                return
            for head in heads:
                if testnext(curr, head):
                    curr[0] += head[0]
                    curr[1] += head[1]
                    locmap[curr[0]][curr[1]] = 1
                    mined.append(grid[curr[0]][curr[1]])
                    dfs(curr)
                    locmap[curr[0]][curr[1]] = 0
                    mined.pop()
                    curr[0] -= head[0]
                    curr[1] -= head[1]
            return
        for x in range(lx):
            for y in range(ly):
                if grid[x][y] != 0:
                    mined = []
                    locmap = [[0 for x in y] for y in grid]
                    locmap[x][y] = 1
                    mined.append(grid[x][y])
                    dfs([x, y])
        return maxgold
