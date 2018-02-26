class Solution:
    def removeElement(self, nums, val):
        con=0
        for x in nums:
            if x!=val:
                nums[con]=x
                con =con + 1
        return con