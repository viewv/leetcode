class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = dict()
        s = 0
        ans = 0
        for i, c in enumerate(hours):
            s += 1 if c > 8 else -1
            if s > 0:
                ans = i + 1
            if s not in res:
                res[s] = i
            if s - 1 in res:
                ans = max(ans, i-res[s-1])
        return ans
