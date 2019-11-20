class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for x in range(l):
            temp = nums[x]
            nums[x] = 0
            for y in range(x + 1, l):
                if nums[y] < temp:
                    nums[x] += 1
        return nums
