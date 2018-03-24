class Solution:
    def isValid(self, s):
        dic = {"()", "[]", "{}"}
        arr = []
        for i in range(0, len(s)):
            if len(arr) != 0 and (arr[-1]+s[i]) in dic:
                arr.pop()
            else:
                arr.append(s[i])
        return len(arr) == 0
