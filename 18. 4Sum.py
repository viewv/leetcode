class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        book = []
        ans = []
        n = len(nums)
        d = dict()
        def ifInd(nums):
            a, b, c, d = nums[0], nums[1], nums[2], nums[3]
            if a in d and b in d[a] and c in d[a][b] and d in d[a][b][c]:
                return True
            else:
                
        def dfs(m, start):
            if m == 4:
                if sum(book) == target:
                    temp = sorted(book)
                    ans.append(temp)
                return
            for x in range(start, n):
                book.append(nums[x])
                dfs(m + 1, x + 1)
                book.pop()
            return
        dfs(0, 0)
        return ans
