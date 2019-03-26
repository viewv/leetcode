def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    bill5 = []
    bill10 = []
    bill20 = []
    for x in bills:
        if x == 5:
            bill5.append(1)
        if x == 10:
            bill10.append(1)
            if len(bill5) == 0:
                return False
            else:
                bill5.pop()
        if x == 20:
            bill20.append(1)
            if len(bill5) == 0:
                return False
            if len(bill10) != 0:
                bill10.pop()
                bill5.pop()
            else:
                if len(bill5) < 3:
                    return False
                else:
                    for y in range(3):
                        bill5.pop()
    return True


print(lemonadeChange([5, 5, 10]))
