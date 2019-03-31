class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1+nums2
        num = sorted(num)
        n = len(num)
        if n % 2 == 0:
            mid = n//2
            return (num[mid-1]+num[mid])/2
        else:
            mid = (n+1)//2
            return num[mid-1]
