from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict.fromkeys(nums, '#')
        for x, n in enumerate(nums):
            if d[n] == '#':
                d[n] = x
            elif d[n] <= x:
                if x - d[n] <= k:
                    return True
                else:
                    d[n] = x
        return False


sol = Solution()
print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))
