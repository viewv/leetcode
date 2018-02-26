#copy from https://leetcode.com/problems/3sum/discuss
# /7392/Python-easy-to-understand-solution-(O(n*n)-time).
#a very good code!
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                #remmber we have been sorted the list
                if s < 0:#s<0 means that we need to make the l bigger
                    l +=1 #l is left
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    #blow code is a way to avoid the duplicate numbers
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res