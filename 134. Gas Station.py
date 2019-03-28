class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length = len(gas)
        diff = 0
        start = 0
        minval = 0
        for x in range(length):
            diff += gas[x] - cost[x]
            if diff < minval:
                minval = diff
                start = x + 1
        if diff < 0:
            return - 1
        return start
