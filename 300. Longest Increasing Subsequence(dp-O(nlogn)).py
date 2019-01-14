class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        length = len(nums)
        for i in range(0, length):
            left = 0
            right = len(dp)
            while left < right:
                mid = left + (right - left) // 2
                if dp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if right >= len(dp):
                dp.append(nums[i])
            else:
                dp[right] = nums[i]
        return len(dp)
