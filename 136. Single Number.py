class Solution:
    def singleNumber(self, nums):
        MAXNUM = 1000000
        all_num_Positve = [0 for x in range(0, MAXNUM)]
        all_num_Negitive = [0 for x in range(0, MAXNUM)]
        for x in(nums):
            if x >= 0:
                all_num_Positve[x] = all_num_Positve[x]+1
            else:
                all_num_Negitive[-1*x] = all_num_Negitive[-1*x]+1
        for index, item in enumerate(all_num_Positve):
            if item == 1:
                return index
        for index, item in enumerate(all_num_Negitive):
            if item == 1:
                return -1*index
