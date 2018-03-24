class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[0:m] + nums2[0:n])
