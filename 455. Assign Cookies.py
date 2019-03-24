class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        ans = 0
        start = 0
        for x in range(0, len(s)):
            for y in range(start, len(g)):
                if s[x] >= g[y]:
                    ans += 1
                    start = y + 1
                    break
        return ans
