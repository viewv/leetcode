class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        length = len(nums)
        tempSum = sum(nums[:k])
        maxSum = tempSum
        for x in range(1, length-k+1):
            tempSum = tempSum - nums[x - 1] + nums[x + k - 1]
            if tempSum > maxSum:
                maxSum = tempSum
        return maxSum / k
