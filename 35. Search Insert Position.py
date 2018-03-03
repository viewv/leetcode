class Solution:
    def searchInsert(self, nums, target):
        nums.append(target)
        nums=sorted(nums)
        for x in range(0,len(nums)):
            if nums[x]==target:
                break
        return x