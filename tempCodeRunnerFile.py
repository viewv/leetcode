def bestdivide(n):
    count = 0
    addnum = 2  # 从2开始
    divide = []
    while count < n:
        count += addnum
        divide.append(addnum)
        addnum += 1
    if count > n:
        count = count - addnum + 1
        differ = n - count
        divide.pop()
    else:
        differ = n - count
    length = len(divide)
    # 减少递归次数，先计算全部的整体要加多少次
    # 之后就不用一次一个加一了
    d = differ // length
    r = differ % length
    for x in range(0, length):
        divide[x] += d
    for x in range(1, r + 1):
        divide[-x] += 1
    return divide


def mult(l):
    # 计算乘积
    ans = 1
    for x in l:
        ans *= x
    return ans


# 简单的测试
divided = bestdivide(133)
ans = mult(divided)
print("List:", divided, "Ans", ans)

# 读取文件模块
with open('output.txt', 'w') as a:
    with open('input.txt', 'r') as f:
        line = f.readline()
        n = int(line)
        n = mult(bestdivide(n))
        a.write(str(n))
