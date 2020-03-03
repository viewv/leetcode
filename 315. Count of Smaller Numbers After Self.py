class Solution(object):
    def countSmaller(self, nums):
        ret = []
        sorted_array = []
        for i in range(len(nums)-1, -1, -1):
            index = bisect.bisect_left(sorted_array, nums[i])
            sorted_array.insert(index, nums[i])
            ret.append(index)
        return ret[::-1]