def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    ans = [1 for x in range(0, len(ratings))]
    for x in range(0, len(ratings) - 1):
        if ratings[x] < ratings[x + 1]:
            ans[x] = 1
        if ratings[x] >= ratings[x + 1]:
            ans[x + 1] = 1
    return sum(ans)


print(candy([1, 3, 2, 2, 1]))
