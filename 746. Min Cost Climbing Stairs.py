class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        dp = [0 for x in range(0, length)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, length):
            # Remember to divided into two cases, if you get into the top of
            # stair like case 1, you don't need to add cost into your dp, but
            # in other cases, you need to do this, add cost into dp
            if i == length - 1:
                dp[i] = min(dp[i - 1], dp[i - 2] + cost[i])
            else:
                dp[i] = min(dp[i - 1] + cost[i], dp[i-2] + cost[i])
        return dp[-1]
