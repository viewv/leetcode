class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if not nums:
            return 0
        if l <= 3:
            return max(nums)
        # dp[start from 0,start from 1]
        dp = [[0, 0] for x in nums]
        dp[0] = nums[0], 0
        dp[1] = max(nums[0], nums[1]), nums[1]
        dp[2] = max(dp[1][0], nums[2] + dp[0][0]), max(nums[1], nums[2])
        for x in range(3, l - 1):
            dp[x] = max(dp[x - 2][0] + nums[x], dp[x - 1][0]
                        ), max(dp[x - 2][1] + nums[x], dp[x - 1][1])
        return max(dp[l-2][0], dp[l-1][1]+nums[l-1])