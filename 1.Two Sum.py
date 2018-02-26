class Solution:
    def twoSum(self, nums, target):
        length=len(nums)
        ans=[0,0]
        for x in range(0,length):
            a=nums[x]
            for y in range(x+1,length):
                b=nums[y]
                if a+b==target:
                    ans[0]=x
                    ans[1]=y
                    return ans