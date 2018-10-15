class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = sorted(set(nums))
        dict = {}
        c = 1
        for n in nums:
            if n - c in dict:
                dict[n-c].append(n)
                c += 1
            else:
                dict[n] = []
                c = 1
        return max(len([a] + b) for a, b in dict.items())
