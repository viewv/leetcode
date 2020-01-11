class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        a = [x for x in range(1, 10)]
        book = [0 for x in range(10)]
        target = n
        ans = []

        def dfs(m, start, k):
            if m == k:
                temp = 0
                temparray = []
                for x in range(0, 9):
                    if book[x] == 1:
                        temp += a[x]
                        temparray.append(a[x])
                if temp == target:
                    ans.append(temparray)
                return
            for x in range(start, 9):
                book[x] = 1
                dfs(m + 1, x + 1, k)
                book[x] = 0
            return
        dfs(0, 0, k)
        return ans
