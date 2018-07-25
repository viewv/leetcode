# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # a = rand7()
        # b = rand7()
        #!WA 1 6/10
        # if a > 3:
        #     return a
        # else:
        #     if b % 2 == 0:
        #         return a + 7
        #     else:
        #         return a
        #!WA 2 8/10
        # return ((rand7()-1)*7+rand7()) % 10+1
        #!WA 3 8/10
        # return (a + b) % 10 + 1
        #!WA 4 4/10
        # a = a % 5
        # b = b % 5
        # return a + b + 1
        #*AC!
        sum = 0
        for x in range(0, 10):
            sum += rand7()
        return sum % 10 + 1

