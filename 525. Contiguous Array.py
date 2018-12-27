class Solution(object):
    def findMaxLength(self, nums):
        dic = {0: -1}
        count = 0
        maxlen = 0
        for x in range(0, len(nums)):
            count += (1 if nums[x] == 1 else - 1)
            if count not in dic:
                dic[count] = x
            else:
                maxlen = max(maxlen, x - dic[count])
        return maxlen
