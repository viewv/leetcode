class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        newTail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
        return newTail + 1