class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        t = 0
        l = [0 for x in range(n)]
        def backtrack(t):
            if t == n:
                temp = []
                for x in range(n):
                    if l[x] == 1:
                        temp.append(nums[x])
                ans.append(temp)
                return
            else:
                l[t] = 1
                backtrack(t+1)
                l[t] = 0
                backtrack(t+1) 
        backtrack(0)
        return ans