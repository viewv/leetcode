class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        point = 0
        end = 0
        while end < len(nums)-1:
            temp = end
            for i in range(point, end+1):
                temp = max(temp, i+nums[i])
            count += 1
            point = end + 1
            end = temp
        return count
