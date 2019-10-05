#
# @lc app=leetcode id=972 lang=python3
#
# [972] Equal Rational Numbers
#

# @lc code=start


class Solution:

    def divminu(self, da, db):
        return {'up': da['up']*db['down']-db['up']*da['down'], 'down': da['down']*db['down']}

    def divplus(self, da, db):
        return {'up': da['up']*db['down']+db['up']*da['down'], 'down': da['down']*db['down']}

    def divsion(self, da, db):
        return {'up': da['up'] * db['down'], 'down': da['down'] * db['up']}

    def getDiv(self, s):
        start = end = pointflag = 0
        length = len(s)
        for i, x in enumerate(s):
            if x == '.':
                pointflag = i
            if x == '(':
                start = i
            if x == ')':
                end = i
        if pointflag == 0:
            return {'up': int(s), 'down': 1}
        elif start == end and start == 0:
            width = length - pointflag - 1
            real = s[:pointflag]
            less = s[pointflag + 1:]
            if less == '':
                return {'up': int(real), 'down': 1}
            else:
                return self.divplus({'up': int(real), 'down': 1}, {'up': int(less), 'down': 10**width})

        else:
            width = end - pointflag - 2
            down = 10 ** width
            repeat = int(s[start + 1:end])
            up = repeat
            real = self.getDiv(s[:start])
            length = end - start - 1
            a1 = {'up': up, 'down': down}
            q = {'up': 1, 'down': 10 ** length}
            one = {'up': 1, 'down': 1}
            res = self.divplus(self.divsion(a1, self.divminu(one, q)), real)
            return res

    def isRationalEqual(self, S: str, T: str) -> bool:
        div_a = self.getDiv(S)
        div_b = self.getDiv(T)
        div = self.divminu(div_a, div_b)
        return bool(div['up'] == 0)
# @lc code=end
