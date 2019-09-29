# from typing import List


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         d = dict.fromkeys(nums, 0)
#         for x in nums:
#             d[x] += 1
#         d = d.items()
#         print(d)
#         d = sorted(d, key=lambda x: x[1], reverse=True)
#         return [x[0] for x in d[:k]]


# sol = Solution()
# print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []

        def back(t):
            if t == N:
                temp = []
                for x in range(0, N):
                    temp.append(nums[x])
                ans.append(temp)
            else:
                for x in range(t, N):
                    temp = nums[x]
                    nums[x] = nums[t]
                    nums[t] = temp
                    back(t+1)
                    temp = nums[x]
                    nums[x] = nums[t]
                    nums[t] = temp
        back(0)
        return ans


sol = Solution()
print(sol.permute([1, 2, 3]))
