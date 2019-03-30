def largestSumAfterKNegations(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    a = sorted(A)
    x = 0
    n = len(A)
    while x < n and K > 0:
        if a[x] < 0:
            a[x] *= -1
            x += 1
            K -= 1
        elif a[x] == 0:
            break
        else:
            if K % 2 == 0:
                break
            else:
                a[x] *= -1
                break
    return sum(a)


print(largestSumAfterKNegations([3, -1, 0, 2], 3))
