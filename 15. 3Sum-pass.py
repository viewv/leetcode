#copy from https://leetcode.com/problems/3sum/discuss
# /7392/Python-easy-to-understand-solution-(O(n*n)-time).
#a very good code!
#I need to learn this code
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()#very import to sort
        for i in range(len(nums)-2):
            #to avoid special input
            #if length of nums is less then 3
            #this for block will not work
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #i must from 1 to end
            #because i<r<l to achieve binery search
            l, r = i+1, len(nums)-1#a special thing in python
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                #remmber we have been sorted the list
                if s < 0:
                    #s<0 means that we need to make the l bigger
                    l +=1 #l is left
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    #blow code is a way to avoid the duplicate numbers
                    #l and r have been add ro the finall anwser
                    #the nums has been sorted so we just have to check
                    #the number nearby
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    #because l and r have changed in to l=l-1
                    #r=r+1, so we must make it correct
                    l += 1; r -= 1
        return res