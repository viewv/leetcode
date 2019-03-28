def canCompleteCircuit(gas, cost):
    length = len(gas)
    fill = 0
    cum = [(x1 - x2) for x1, x2 in zip(gas, cost)]
    start = cum.index(max(cum))
    if cum[start] < 0:
        return - 1
    cur = start
    while (cur + 1) % length != start:
        cur = cur % length
        fill = fill + gas[cur] - cost[cur]
        if fill < 0:
            return - 1
        cur += 1
    if fill + gas[cur] - cost[cur] >= 0:
        return start
    return - 1


print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))
