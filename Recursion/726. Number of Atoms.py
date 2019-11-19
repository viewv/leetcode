class Solution:
    def countOfAtoms(self, formula: str) -> str:
        atoms = dict()

        def fun(s, times):
            l = len(s)
            x = 0
            while x < l:
                if s[x].isupper():
                    if x == l - 1:
                        loc = 0
                    elif s[x + 1].isdigit():
                        loc = 3
                        end = x
                        for y in range(x + 1, l):
                            if s[y].isdigit():
                                end += 1
                            else:
                                break
                    elif s[x + 1].isupper():
                        loc = 0
                    elif s[x + 1].islower():
                        loc = 1
                        if x + 1 == l - 1:
                            loc = 1
                        elif s[x + 2].isdigit():
                            loc = 2
                            end = x + 1
                            for y in range(x + 2, l):
                                if s[y].isdigit():
                                    end += 1
                                else:
                                    break
                        elif s[x + 2].isupper():
                            loc = 1
                    else:
                        loc = 0
                    if loc == 0:
                        alp, num = s[x], 1
                    elif loc == 1:
                        alp, num = s[x: x + 2], 1
                    elif loc == 2:
                        alp, num = s[x: x + 2], int(s[x + 2:end+1])
                    elif loc == 3:
                        alp, num = s[x: x+1], int(s[x+1:end+1])
                    if alp in atoms:
                        atoms[alp] += num * times
                    else:
                        atoms[alp] = num * times
                elif s[x] == '(':
                    flag = 1
                    for y in range(x+1, l):
                        if s[y] == '(':
                            flag += 1
                        if s[y] == ')':
                            flag -= 1
                        if flag == 0:
                            if y == l - 1:
                                num = 1
                            elif s[y+1].isdigit():
                                end = y
                                for z in range(y + 1, l):
                                    if s[z].isdigit():
                                        end += 1
                                    else:
                                        break
                                num = int(s[y + 1: end + 1])
                            else:
                                num = 1
                            fun(s[x + 1: y], num * times)
                            x = y
                            break
                x += 1
        fun(formula, 1)

        def foo(v):
            if v == 1:
                return ''
            else:
                return str(v)
        list_atom = [[k, foo(v)] for k, v in atoms.items()]
        list_atom = sorted(list_atom, key=(lambda x: x[0]))
        list_atom = [''.join(v) for v in list_atom]
        ans = ''.join(list_atom)
        return ans
