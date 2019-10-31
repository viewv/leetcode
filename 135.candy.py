#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        if length == 0:
            return 0
        if length == 1:
            return 1
        # print("length:",length)
        ans = [1 for x in range(length)]
        minist_rate = ratings[0]
        loc = 0
        for i, c in enumerate(ratings):
            if c < minist_rate:
                loc = i
                minist_rate = c
        ans[loc] = 1

        for x in range(loc + 1, length - 1):
            left = ratings[x - 1]
            if ratings[x] > left:
                ans[x] = ans[x - 1] + 1
            elif ratings[x] < left:
                ans[x] = 1
            else:
                ans[x] = ans[x - 1]
        
        for x in range(loc - 1, 0, -1):
            right = ratings[x + 1]
            if ratings[x] > right[]

        # if ratings[0] > ratings[1]:
        #     ans[0] = 2
        # if ratings[-1] > ratings[-2]:
        #     ans[-1] = 2

                # @lc code=end
