from itertools import product, compress


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        for pattern in product((0, 1), repeat=len(candidates)):
            temp = list(compress(candidates, pattern))
            if sum(temp) == target:
                ans.append(temp)
