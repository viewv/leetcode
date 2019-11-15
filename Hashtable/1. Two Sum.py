class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        waitset = dict()
        for i, c in enumerate(nums):
            if c in waitset:
                return [waitset[c], i]
            else:
                waitset[target-c] = i
