#copy from
#https://leetcode.com/problems/3sum/discuss/7393/
#Straight-forward-Python-AC-O(n2)-
#solution-with-decent-explanation
#even though it is tle but the thought is good
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) <3: # deal with special input
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]

        nums = sorted(nums) # sorted, O(nlgn)
        ans = []

        for i in range(len(nums) -2):
            j = i+1
            k = len(nums) -1 # hence i < j < k

            while j<k: # if not cross line
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum == 0:
                    ans.append((nums[i], nums[j], nums[k]))

                if temp_sum > 0: 
                    # which means we need smaller sum, 
                    # move k backward, remember we sort the array
                    k -= 1
                else:
                    j += 1

        return list(set(tuple(ans))) 
        # I bet this is not the best way to 
        # eliminate duplicate solutions