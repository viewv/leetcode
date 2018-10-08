class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s, e = 0, len(nums) - 1

        while True:
            mid = (s + e) // 2

            left = nums[mid-1] if mid-1 >= 0 else float('-inf')
            right = nums[mid+1] if mid+1 < len(nums) else float('-inf')

            if left < nums[mid] and right < nums[mid]:
                return mid
            elif nums[mid] < right:
                s = mid + 1
            else:
                e = mid - 1
