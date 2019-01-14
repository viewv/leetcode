class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        maxlength = 1
        if length == 0:
            return 0
        for x in range(0, length - 1):
            start = x
            templength = 1
            for y in range(x + 1, length):
                if nums[y] > nums[start]:
                    templength += 1
                    start = y
                else:
                    break
            if templength > maxlength:
                maxlength = templength
        return maxlength
