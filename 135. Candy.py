#! Try To tFinish This
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ans = [1 for x in range(0, len(ratings))]
        for x in range(0, len(ratings) - 1):
            if ratings[x + 1] > ratings[x]:
                ratings[x + 1] = ratings[x] + 1
            if ratings[x + 1] < ratings[x]:
                ratings[x] = ratings[x + 1] + 1
        return sum(ans)
