from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        book = []
        ans = []
        n = len(nums)

        def dfs(m, start):
            if m == 4:
                if sum(book) == target:
                    temp = [x for x in book]
                    ans.append(temp)
                return
            for x in range(start, n):
                book.append(nums[x])
                dfs(m + 1, x + 1)
                book.pop()
            return
        dfs(0, 0)
        return ans



sol = Solution()

print(sol.fourSum([1, 0, -1, 0, -2, 2],0))
