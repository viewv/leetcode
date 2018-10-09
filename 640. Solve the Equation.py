import re


class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        numsAll = re.split(r'([+-=x])', equation)
        print(numsAll)
        nums = []
        for x in numsAll:
            if x != '':
                nums.append(x)
        print(nums)
        flag = check = 1
        number = 0
        ex = 0
        for x in range(0, len(nums)):
            if nums[x] == '=':
                flag = -1
                check = 1
            elif nums[x] == '-':
                check = -1
            elif nums[x] == '+':
                check = 1
            else:
                if nums[x] == 'x':
                    if x == 0:
                        ex += flag * 1
                    elif nums[x - 1] == '+' or nums[x - 1] == '=':
                        ex += flag * 1
                    elif nums[x - 1] == '-':
                        ex -= flag * 1
                        check = 1
                    else:
                        continue
                elif x == len(nums) - 1:
                    number += -1*flag*check*int(nums[x])
                elif nums[x + 1] == 'x':
                    ex += flag * check * (int(nums[x]))
                else:
                    number += -1 * flag * check * (int(nums[x]))
        if ex == 0 and number == 0:
            return "Infinite solutions"
        elif ex == 0:
            return "No solution"
        else:
            return "x="+str(int(number/ex))


s = "x=20"
ans = Solution()
print(ans.solveEquation(s))
