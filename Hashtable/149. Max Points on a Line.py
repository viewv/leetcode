import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        maxl = 0
        for x in range(l):
            p = points[x]
            slopedict = dict()
            for y in range(l):
                q = points[y]
                i = p[0] - q[0]
                j = p[1] - p[1]
                gcd = math.gcd(i, j)
                i //= gcd
                j //= gcd
                slope = [i, j]
                if slope in slopedict:
                    slopedict[slope] += 1
                    if slopedict[slope] > maxl:
                        maxl = slopedict[slope]
                else:
                    slopedict[slope] = 1
        return maxl
