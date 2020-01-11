class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        now = nums[0]
        times = 1
        l = len(nums)
        for x in range(1:l):
            if nums[x] == now:
                times += 1
            if nums[x] != now:
                if times == 1:
                    return now
                else:
                    times = 1
                    now = nums[x]
                    