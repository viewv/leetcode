class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = [[nums[0], 1]]
        temp = [-1, -1]
        for x in nums[1:]:
            if x != n[-1][0]:
                n.append([x, 1])
            else:
                n[-1][1] += 1
        for x in n:
            if x[1] >= temp[1]:
                temp = x
        return temp[0]
