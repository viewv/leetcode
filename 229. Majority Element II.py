from typing import List
# * majority vote Algo.


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count0 = count1 = 0
        target0 = target1 = 0
        length = len(nums)
        for x in range(length):
            if nums[x] == target0:
                count0 += 1
            elif nums[x] == target1:
                count1 += 1
            elif count0 == 0:
                count0 += 1
                target0 = nums[x]
            elif count1 == 0:
                count1 += 1
                target1 = nums[x]
            else:
                count0 -= 1
                count1 -= 1
        count0 = 0
        count1 = 0
        for x in range(length):
            if nums[x] == target0:
                count0 += 1
            #!important to have a elif if!
            #!to avoid target0 == target1 and get two answer!
            elif nums[x] == target1:
                count1 += 1
        ans = []
        k = length // 3
        if count0 > k:
            ans.append(target0)
        if count1 > k:
            ans.append(target1)
        return ans
