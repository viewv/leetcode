#Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums):
        maxEndingHere = maxSum = nums[0]
        for i in range(1, len(nums)):
            maxEndingHere = max(nums[i], maxEndingHere + nums[i])
            maxSum = max(maxEndingHere, maxSum)
        return maxSum
            