class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [1 for x in range(0, length)]
        for x in range(0, length):
            for y in range(0, x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y] + 1)
            maxlength = max(maxlength, dp[x])
        return maxlength
