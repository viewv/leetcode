ans = []


def seq(string):
    if len(string) == 1:
        return string
    else:
        a = string[0:1]
        ans.append(a + seq(string[1:]))
        ans.append(seq(string[1:]) + a)


seq("abcde")

print(ans)
