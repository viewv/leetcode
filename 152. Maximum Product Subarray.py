class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_min = current_max = max_so_far = nums[0]

        for i in range(1, len(nums)):
            temp = current_max
            current_max = max(nums[i], current_min *
                              nums[i], current_max * nums[i])
            current_min = min(nums[i], current_min * nums[i], temp * nums[i])

            max_so_far = max(current_max, max_so_far)

        return max_so_far
