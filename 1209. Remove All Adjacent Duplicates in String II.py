class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) <= 1:
            return s
        s = list(s)
        flag = 0
        curr = s[0]
        counter = 1
        start = 0
        i = 0
        l = len(s)
        while True:
            i += 1
            if s[i] == curr:
                counter += 1
            if counter == k:
                for x in range(start, i+1):
                    s.pop(start)
                flag = 1
                l -= k
                if start == 0:
                    i = 0
                else:
                    i = start - 1
                start = i
                curr = s[i]
                counter = 1
            if s[i] != curr:
                curr = s[i]
                start = i
                counter = 1
            if i == l - 1:
                if flag == 1:
                    l = len(s)
                    i = 0
                    flag = 0
                    start = 0
                    counter = 1
                    curr = s[0]
                else:
                    break
        return ''.join(s)
