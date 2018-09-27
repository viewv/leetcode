class Solution:
    def count(self, a, num):
        con = 0
        for x in a:
            if x == num:
                con += 1
        return con

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        number0 = self.count(nums, 0)
        number1 = self.count(nums, 1)
        number2 = self.count(nums, 2)
        length = number0 + number1 + number2
        for x in range(0, length):
            if x < number0:
                nums[x] = 0
            elif x > number0 and x < number0 + number1:
                nums[x] = 1
            else:
                nums[x] = 2
