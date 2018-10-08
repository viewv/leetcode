class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        m = sum(nums)-sum(set(nums))
        dif = (n*(n+1))//2-sum(set(nums))
        return [m, dif]
