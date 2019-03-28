def removeKdigits(num, k):
    numlength = len(num)
    number = [int(x) for x in list(num)]
    finalength = numlength - k
    if finalength <= 0:
        return "0"
    start = 0
    a = start
    ans = []
    ctrl = 0
    need = finalength
    b = numlength - need + 1
    while ctrl < numlength - k:
        temp = number[start]
        a = start
        for x in range(a, b):
            if temp > number[x]:
                temp = number[x]
                start = x
        ans.append(number[start])
        ctrl += 1
        start += 1
        need -= 1
        b = numlength - need + 1
    ans = [str(x) for x in ans]
    ans = ''.join(ans)
    ans = int(ans)
    ans = str(ans)
    return ans


print(removeKdigits("1107", 1))
