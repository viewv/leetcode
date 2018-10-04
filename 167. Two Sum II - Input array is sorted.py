class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        for x in range(0, length):
            t = target - numbers[x]
            flag = self.search(numbers[(x + 1):], t)
            if flag != -1:
                return [x + 1, flag + x + 2]

    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1
