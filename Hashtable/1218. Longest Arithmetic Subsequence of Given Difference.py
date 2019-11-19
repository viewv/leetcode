class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        res = {}
        for num in arr:
            res[num] = res[num - diff] + 1 if (num - diff) in res else 1
        return max(res.values())
