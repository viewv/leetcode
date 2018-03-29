class Solution(object):
    def splitArraySameAverage(self, A):
        nAll=len(A)
        ave=sum(A)//nAll
        for x in range(1,nAll):
            for y in range(1,nAll):
                tempst=A[y]
                for z in range(y,nAll):
                    pass   