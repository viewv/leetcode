from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict.fromkeys(nums, 0)
        for x in nums:
            d[x] += 1
        d = d.items()
        print(d)
        d = sorted(d, key=lambda x: x[1], reverse=True)
        return [x[0] for x in d[:k]]


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
