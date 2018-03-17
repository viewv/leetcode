class Solution:
    def generate(self, numRows):
        pas = [[1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return pas
        else:
            for i in range(2, numRows + 1):
                a = []
                for j in range(i):
                    if j == 0 or j == i - 1:
                        a.append(1)
                    else:
                        a.append(pas[i - 2][j - 1] + pas[i - 2][j])
                pas.append(a)
        return pas