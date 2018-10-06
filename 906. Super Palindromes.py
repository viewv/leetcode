class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        start = int(L)
        end = int(R)
        ans = 0
        for x in range(start, end + 1):
            if self.isPalindrom(x):
                temp = int(x ** 0.5)
                if temp ** 2 == x and self.isPalindrom(temp):
                    ans += 1
        return ans
            

    def isPalindrom(self, n):
        string = str(n)
        if string == string[::-1]:
            return True
        else:
            return False