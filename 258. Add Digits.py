class Solution:
    def addDigits(self, num):
        snum = str(num)
        if len(snum) == 1:
            return num
        sum = 0
        for i in snum:
            sum += int(i)
            if sum > 9:
                sum -= 9
        return sum
