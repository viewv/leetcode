class Solution:
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        sequence=[1]*n
        sequence[1]=2
        for x in range(2,n):
            sequence[x]=sequence[x-1]+sequence[x-2]
        return sequence[n-1]