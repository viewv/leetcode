class Solution:
    def rotate(self, nums, k):
        rot = k % len(nums)
        if rot > 0:
            nums[:] = nums[-rot:] + nums[:len(nums)-rot]
