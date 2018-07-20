def spiralOrder(matrix):
    x = 0
    y = 0
    point = 0
    count = 0
    ans = []
    xdistion = [1, 0, -1, 0]
    ydistion = [0, 1, 0, -1]
    h = len(matrix)
    l = len(matrix[0])
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


matrix = [[3], [2]]

ans = spiralOrder(matrix)
print(ans)
