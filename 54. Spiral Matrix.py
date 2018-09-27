class Solution:
    def spiralOrder(self, matrix):
        x = 0
        y = 0
        point = 0
        count = 0
        ans = []
        xdistion = [1, 0, -1, 0]
        ydistion = [0, 1, 0, -1]
        h = len(matrix)
        if h == 0:
            return ans
        l = len(matrix[0])
        if l == 1:
            for x in matrix:
                ans.append(x[0])
            return ans
        xdis = 0
        ydis = 0
        size = h * l
        while count < size:
            ans.append(matrix[y][x])
            xdis = xdistion[point]
            ydis = ydistion[point]
            matrix[y][x] = None
            count += 1
            x = x + xdis
            y = y + ydis
            if x + xdis >= l or y + ydis >= h or x + xdis < 0 or y + ydis < 0:
                point += 1
                point = point % 4
            elif matrix[y + ydis][x + xdis] == None:
                point += 1
                point = point % 4
            else:
                pass
        return ans
